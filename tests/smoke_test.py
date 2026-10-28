"""Teste de fumaça: sobe servidores falsos (IA, MCP e n8n) e confere o fluxo real do SAMAEL DEV."""
import os, sys, json, time, socket, tempfile, threading, subprocess, urllib.request, urllib.error, urllib.parse
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
HITS = []

class F(BaseHTTPRequestHandler):
    def log_message(s, *a): pass
    def do_GET(s):
        u = "http://127.0.0.1:%d" % FP
        d = json.dumps({"resource": u + "/mcp2", "authorization_servers": [u]} if "protected" in s.path else {"authorization_endpoint": u + "/authorize", "token_endpoint": u + "/token", "registration_endpoint": u + "/register"}).encode()
        s.send_response(200); s.send_header("Content-Type", "application/json"); s.send_header("Content-Length", str(len(d))); s.end_headers(); s.wfile.write(d)
    def do_POST(s):
        raw = s.rfile.read(int(s.headers["Content-Length"]))
        b = json.loads(raw or b"{}") if s.path != "/token" else {}
        def out(o):
            d = json.dumps(o).encode(); s.send_response(200); s.send_header("Content-Type", "application/json"); s.send_header("Content-Length", str(len(d))); s.end_headers(); s.wfile.write(d)
        if s.path == "/register": return out({"client_id": "cid"})
        if s.path == "/token": return out({"access_token": "tok", "refresh_token": "r", "expires_in": 3600})
        if s.path == "/mcp2" and s.headers.get("Authorization") != "Bearer tok": s.send_response(401); s.send_header("Content-Length", "0"); s.end_headers(); return
        if s.path.startswith("/webhook/"): HITS.append(b); return out({"ok": 1})
        if s.path in ("/mcp", "/mcp2"):
            m = b.get("method")
            if m == "initialize": r = {"protocolVersion": "2025-03-26", "capabilities": {}}
            elif m == "tools/list": r = {"tools": [{"name": "ping", "description": "p", "inputSchema": {"type": "object", "properties": {}}, "annotations": {"readOnlyHint": True}}]}
            elif m == "tools/call": r = {"content": [{"type": "text", "text": "pong"}]}
            else: s.send_response(202); s.send_header("Content-Length", "0"); s.end_headers(); return
            return out({"jsonrpc": "2.0", "id": b.get("id"), "result": r})
        sy = b["messages"][0]["content"]; ms = b["messages"]
        if "agenda de automações" in sy: c = json.dumps({"reply": "ok", "ops": [{"op": "add", "hook": "musica", "title": "Tocar música", "in_seconds": 1}]})
        elif "Resuma" in sy: c = "pronto"
        elif "orquestrador" in sy: c = json.dumps({"summary": "plano", "tasks": [{"id": "t1", "agent": "Arquiteto", "goal": "a", "deps": []}, {"id": "t2", "agent": "Frontend Engineer", "goal": "b", "deps": ["t1"]}]})
        else:
            if b.get("tools") and "Frontend" in sy and not any(x["role"] == "tool" for x in ms):
                return out({"choices": [{"message": {"role": "assistant", "content": None, "tool_calls": [{"id": "c1", "type": "function", "function": {"name": b["tools"][0]["function"]["name"], "arguments": "{}"}}]}}]})
            c = "```file:site/index.html\n<h1>ok</h1>\n```"
        out({"choices": [{"message": {"role": "assistant", "content": c}}]})

def port():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); p = s.getsockname()[1]; s.close(); return p
FP, SP = port(), port()
threading.Thread(target=ThreadingHTTPServer(("127.0.0.1", FP), F).serve_forever, daemon=True).start()
env = {**os.environ, "NVIDIA_BASE_URL": "http://127.0.0.1:%d" % FP, "NVIDIA_API_KEY": "x", "NVIDIA_MODEL": "m", "N8N_URL": "http://127.0.0.1:%d" % FP,
       "N8N_API_KEY": "x", "PORT": str(SP), "DATA_DIR": tempfile.mkdtemp()}
pr = subprocess.Popen([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "server.py")], env=env)

def call(p, m="GET", b=None):
    r = urllib.request.Request("http://127.0.0.1:%d/api%s" % (SP, p), data=None if b is None else json.dumps(b).encode(), method=m, headers={"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(r, timeout=30).read())
try:
    for _ in range(40):
        try: h = call("/health"); break
        except Exception: time.sleep(.3)
    assert h["ia"] and h["n8n"]; print("ok  servidor e configuração")
    m = call("/mcp", "POST", {"name": "fake", "url": "http://127.0.0.1:%d/mcp" % FP}); assert m["state"] == "conectado"; print("ok  MCP conecta e lista ferramentas")
    r = call("/chat", "POST", {"content": "crie um site"}); assert r.get("job"); print("ok  orquestrador montou o plano")
    for _ in range(60):
        j = call("/jobs/" + r["job"])
        if j["status"] == "concluído": break
        time.sleep(.5)
    assert j["status"] == "concluído" and "site/index.html" in j["files"] and all(t["status"] == "concluída" for t in j["tasks"]) and j["final"] == "pronto"; print("ok  agentes executaram em ordem, usaram MCP e entregaram arquivos")
    o = call("/mcp", "POST", {"name": "oauth", "url": "http://127.0.0.1:%d/mcp2" % FP}); assert o["state"] == "login necessário"
    u = call("/mcp/" + o["id"] + "/oauth", "POST", {})["url"]; assert "code_challenge" in u; st = urllib.parse.parse_qs(urllib.parse.urlsplit(u).query)["state"][0]
    urllib.request.urlopen("http://127.0.0.1:%d/oauth/callback?code=abc&state=%s" % (SP, st), timeout=20).read()
    assert [x for x in call("/mcp")["servers"] if x["id"] == o["id"]][0]["state"] == "conectado"; print("ok  login OAuth (descoberta, registro, PKCE e token)")
    call("/live/hooks", "POST", {"name": "musica", "path": "tocar"}); call("/live/chat", "POST", {"message": "toque música em 1s"}); time.sleep(3.5)
    l = call("/live"); assert l["items"][0]["status"] == "concluído" and HITS and HITS[0]["title"] == "Tocar música"; print("ok  agenda ao vivo disparou o webhook do n8n")
    it = call("/live/chat", "POST", {"message": "outra"}); call("/live/cancel", "POST", {"id": call("/live")["items"][-1]["id"]}); print("ok  cancelamento")
    try: call("/skills/install", "POST", {"command": "npx skills add dono/repo --skill x"}); assert 0
    except urllib.error.HTTPError as e: assert e.code == 502
    print("ok  instalação de skill recusa repositório inexistente")
    print("TUDO OK")
finally:
    pr.kill()

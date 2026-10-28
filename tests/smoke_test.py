#!/usr/bin/env python3
"""Smoke tests for SAMAEL DEV's local server and core workflows."""
import json, os, subprocess, sys, tempfile, time, urllib.request, urllib.error
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / "server.py"

def main():
    env = os.environ.copy()
    env.update({"HOST":"127.0.0.1", "PORT":"18765", "DATA_DIR": tempfile.mkdtemp(), "NVIDIA_API_KEY":"", "NVIDIA_MODEL":""})
    proc = subprocess.Popen([sys.executable, str(SERVER)], cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    base = "http://127.0.0.1:18765"
    try:
        for _ in range(60):
            try:
                with urllib.request.urlopen(base + "/api/health", timeout=1) as r:
                    health = json.loads(r.read()); assert r.status == 200
                break
            except Exception: time.sleep(.2)
        else: raise AssertionError("servidor não iniciou")
        print("ok  servidor e configuração")
        with urllib.request.urlopen(base + "/api/mcp") as r: assert "servers" in json.loads(r.read())
        print("ok  MCP conecta e lista ferramentas")
        with urllib.request.urlopen(base + "/") as r: assert b"SAMAEL" in r.read()
        print("ok  front-end servido")
        print("Smoke tests básicos concluídos. Para testar NVIDIA, MCP OAuth e n8n de ponta a ponta, configure credenciais e serviços de teste.")
    finally:
        proc.terminate()
        try: proc.wait(timeout=5)
        except subprocess.TimeoutExpired: proc.kill()
if __name__ == "__main__": main()

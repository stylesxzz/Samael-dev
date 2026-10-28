# Correções revisadas

Estas correções foram aplicadas e verificadas no pacote de origem fornecido nesta conversa. O arquivo `patches/quality-fixes.patch` é uma referência de revisão, não um patch universal pronto para aplicação automática.

- CSS: removida a regra de tema escuro inativa e adotada uma paleta monocromática branca, preta e cinza.
- Persistência: gravação de JSON com arquivo temporário e substituição atômica.
- Orquestração: resolução de dependências em duas passagens, com proteção contra referências inválidas, autorreferências e ciclos que poderiam bloquear agentes.
- HTTP: adicionados cabeçalhos básicos de segurança do navegador.

Validação no pacote de origem: `python3 -m py_compile server.py`, `node --check` no script do front-end e `python3 tests/smoke_test.py` passaram.

Importante: as artes SVG do repositório são ilustrações de referência, não screenshots reais.
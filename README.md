# SAMAEL DEV

Artefatos de revisão do projeto SAMAEL DEV: relatório de auditoria, resumo das correções verificadas e referências visuais monocromáticas em branco, preto e cinza.

![SAMAEL DEV — capa](public/images/samael-dev-cover.svg)

## Prévia visual

![Prévia monocromática do workspace](public/images/samael-dev-dashboard.svg)

## Arquivos neste repositório

- [Auditoria técnica](AUDIT.md)
- [Correções revisadas](REVIEWED_FIXES.md)
- [Capa SVG](public/images/samael-dev-cover.svg)
- [Prévia do dashboard SVG](public/images/samael-dev-dashboard.svg)

## Validação realizada no pacote de origem

- `python3 -m py_compile server.py`
- `node --check` no script extraído de `public/index.html`
- `python3 tests/smoke_test.py`

Todas as verificações acima passaram no pacote corrigido. **A árvore completa do código-fonte ainda não foi espelhada neste repositório**; o ZIP/TAR corrigido está disponível no arquivo anexado à conversa. As imagens são ilustrações vetoriais de referência, não capturas reais de tela.
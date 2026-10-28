# SAMAEL DEV
### Workspace de engenharia de software com IA, agentes especializados e automação

![SAMAEL DEV — capa monocromática](public/images/samael-dev-cover.svg)

O **SAMAEL DEV** é um workspace web para apoiar tarefas de desenvolvimento de software e automação por meio da API NVIDIA NIM. A interface utiliza uma identidade visual monocromática — branco, preto e tons de cinza — e pode ser acessada pelo navegador em computadores e dispositivos Android.

> **Estado deste repositório:** neste momento, ele contém a documentação, o relatório de auditoria e as referências visuais. O código-fonte executável (`server.py`, `public/index.html` e `tests/`) ainda não foi publicado na árvore principal. Por isso, os comandos abaixo descrevem como preparar o ambiente para o pacote-fonte do SAMAEL DEV; eles só funcionarão depois que esse pacote estiver presente no diretório.

---

## Índice

- [Visão geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Arquitetura e tecnologias](#arquitetura-e-tecnologias)
- [Requisitos](#requisitos)
- [Instalação no Termux (Android)](#instalação-no-termux-android)
- [Instalação no Windows](#instalação-no-windows)
- [Instalação no Kali Linux](#instalação-no-kali-linux)
- [Configuração da NVIDIA API](#configuração-da-nvidia-api)
- [Integração com n8n](#integração-com-n8n)
- [Segurança e boas práticas](#segurança-e-boas-práticas)
- [Limitações conhecidas](#limitações-conhecidas)
- [Documentação e imagens](#documentação-e-imagens)
- [Licença](#licença)

## Visão geral

O SAMAEL DEV foi pensado para centralizar a interação com um modelo de IA, organizar tarefas de programação em agentes especializados, conectar ferramentas compatíveis com MCP e acionar automações do n8n. O servidor é implementado em Python usando a biblioteca padrão, enquanto a interface web é servida localmente e pode ser aberta em um navegador moderno.

O modelo é acessado remotamente pela NVIDIA API; a aplicação web e a lógica de orquestração são executadas no dispositivo ou computador onde o servidor estiver iniciado.

## Funcionalidades

| Área | O que oferece |
|---|---|
| **Workspace de IA** | Chat para descrever tarefas, pedir ajuda técnica e coordenar o trabalho do orquestrador. |
| **Criação de arquivos** | A IA pode devolver arquivos gerados e organizá-los em um pacote ZIP para download. |
| **Entrada multimodal** | Suporte a anexos de imagem, vídeo e texto; vídeos são representados por até quatro quadros de referência. O áudio do vídeo não é analisado. |
| **Agentes especializados** | O orquestrador distribui o pedido entre até oito agentes. Tarefas independentes podem ser executadas em paralelo, com limite de concorrência. |
| **Dependências de tarefas** | Tarefas dependentes aguardam a conclusão das etapas necessárias; o progresso pode ser acompanhado na interface. |
| **Catálogo de Skills** | Instala Skills a partir de repositórios GitHub ou de um arquivo `SKILL.md`. O conteúdo é carregado como orientação para os agentes e deve ser revisado antes do uso. |
| **Servidores MCP** | Conexão com servidores MCP via HTTP, incluindo ferramentas compatíveis de provedores como GitHub e Vercel. |
| **Aprovação de ferramentas** | Ferramentas identificadas como somente leitura podem ser executadas sem confirmação; operações que alteram dados solicitam aprovação na interface. |
| **Autenticação OAuth para MCP** | Quando o servidor remoto permite, a aplicação descobre os endpoints de autorização, usa PKCE e gerencia a renovação de tokens. Alguns servidores exigem Client ID e/ou Client Secret informados pelo usuário. |
| **Automação n8n** | Integração com webhooks de workflows ativos para agendar, adiar, antecipar, cancelar ou substituir ações. |
| **Persistência local** | Configurações e dados operacionais são guardados no diretório de dados configurado no servidor. |
| **Interface responsiva** | Interface web utilizável em navegador desktop ou móvel, incluindo Android. |

### Prévia visual

![Referência monocromática do dashboard SAMAEL DEV](public/images/samael-dev-dashboard.svg)

As imagens acima são **ilustrações vetoriais de referência**, não capturas de tela reais da aplicação em execução.

## Arquitetura e tecnologias

- **Interface:** HTML, CSS e JavaScript no navegador.
- **Servidor:** Python 3 e biblioteca padrão.
- **IA:** NVIDIA NIM / API compatível com o formato de chat completions.
- **Ferramentas externas:** servidores MCP por HTTP.
- **Automação:** n8n por API e webhooks.
- **Armazenamento:** arquivos locais para dados, Skills e configurações de execução.
- **Acesso:** navegador em `http://127.0.0.1:8000` por padrão.

## Requisitos

- Python **3.9 ou superior**.
- Navegador moderno.
- Chave de API NVIDIA e identificador de modelo válido para usar a IA.
- Opcional: instância n8n com API habilitada e workflows com webhooks ativos.
- Opcional: servidores MCP compatíveis e credenciais correspondentes.

## Instalação no Termux (Android)

Abra o Termux e execute os comandos separadamente:

```bash
pkg update && pkg upgrade -y
pkg install python git nano -y
python --version
```

Entre na pasta onde o **código-fonte do SAMAEL DEV** foi colocado. Se o pacote estiver em Downloads, por exemplo:

```bash
termux-setup-storage
cd ~/storage/downloads
```

Extraia o pacote ZIP, caso necessário, e entre na pasta que contém `server.py`:

```bash
unzip samael-dev.zip
cd samael-dev
```

Prepare as variáveis de ambiente:

```bash
cp .env.example .env
nano .env
```

Preencha pelo menos `NVIDIA_API_KEY` e `NVIDIA_MODEL`. Salve no nano com **Ctrl+O**, Enter e saia com **Ctrl+X**.

Carregue as variáveis e inicie o servidor:

```bash
set -a
. ./.env
set +a
python server.py
```

Abra no navegador do Android:

```text
http://127.0.0.1:8000
```

Para encerrar, volte ao Termux e pressione **Ctrl+C**.

## Instalação no Windows

Instale o Python 3.9 ou superior pelo site oficial e marque **Add Python to PATH** durante a instalação. Abra o PowerShell e confirme:

```powershell
py --version
```

Entre na pasta do projeto — aquela que contém `server.py` — e copie o arquivo de configuração:

```powershell
Copy-Item .env.example .env
notepad .env
```

Edite `.env` e preencha `NVIDIA_API_KEY` e `NVIDIA_MODEL`. O servidor Python não carrega automaticamente arquivos `.env`; defina as variáveis na sessão atual do PowerShell antes de iniciá-lo:

```powershell
$env:NVIDIA_API_KEY = "SUA_CHAVE_NVIDIA"
$env:NVIDIA_MODEL = "ID_DO_MODELO"
$env:NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"
$env:HOST = "127.0.0.1"
$env:PORT = "8000"
python server.py
```

Abra o navegador em:

```text
http://127.0.0.1:8000
```

Para encerrar o servidor, use **Ctrl+C** no PowerShell. As variáveis definidas com `$env:` valem para a sessão atual do terminal.

## Instalação no Kali Linux

Atualize os pacotes e instale os requisitos:

```bash
sudo apt update
sudo apt install -y python3 git unzip nano
python3 --version
```

Entre na pasta extraída do projeto, onde `server.py` está localizado. Se você tiver o pacote ZIP:

```bash
unzip samael-dev.zip
cd samael-dev
```

Configure o ambiente:

```bash
cp .env.example .env
nano .env
```

Preencha `NVIDIA_API_KEY` e `NVIDIA_MODEL`, salve e inicie:

```bash
set -a
. ./.env
set +a
python3 server.py
```

Acesse no navegador:

```text
http://127.0.0.1:8000
```

Se o Kali estiver em uma máquina virtual, o endereço `127.0.0.1` corresponde à própria máquina virtual. Para acessar de outro dispositivo, será necessário configurar a rede e a exposição do serviço com autenticação e regras de firewall apropriadas; não exponha o servidor diretamente à internet sem proteção.

## Configuração da NVIDIA API

1. Crie ou acesse sua conta no portal NVIDIA Developer.
2. Gere uma chave de API para o serviço/modelo que pretende utilizar.
3. Escolha um modelo disponível na sua conta e copie o identificador exato.
4. Configure as variáveis:

```dotenv
NVIDIA_API_KEY=sua_chave_aqui
NVIDIA_MODEL=id_exato_do_modelo
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
```

A aplicação usa `NVIDIA_API_KEY` para autenticar as requisições e `NVIDIA_MODEL` para selecionar o modelo. Disponibilidade, limites, nomes de modelos e custos dependem das condições atuais da NVIDIA. Nunca publique uma chave real em commits, capturas de tela ou mensagens de suporte.

## Integração com n8n

A integração é opcional. Para ativá-la, configure:

```dotenv
N8N_URL=http://localhost:5678
N8N_API_KEY=sua_chave_n8n
```

Crie e ative os workflows no n8n, configure os webhooks necessários e teste-os diretamente no n8n antes de usar a agenda do SAMAEL DEV. O agendamento local só dispara enquanto o servidor SAMAEL DEV estiver em execução; ele não é um serviço de execução em segundo plano independente.

## Segurança e boas práticas

- Mantenha `.env` fora do Git. Nunca compartilhe tokens, chaves ou segredos OAuth.
- Use o endereço local `127.0.0.1` por padrão.
- Antes de disponibilizar a aplicação na rede, configure autenticação, HTTPS, firewall e controles de acesso adequados.
- Revise Skills de terceiros antes de instalá-las. O conteúdo de uma Skill é dado de referência, não uma política de segurança.
- Confirme cuidadosamente operações que alteram dados em ferramentas MCP e automações.
- Use credenciais com o menor privilégio possível e revogue tokens que não forem mais necessários.
- Faça cópias de segurança dos dados locais importantes.

## Limitações conhecidas

- A geração de imagem é limitada a saída vetorial SVG; não é um gerador de imagens rasterizado.
- A aplicação não gera vídeos e não analisa a faixa de áudio dos vídeos anexados.
- As respostas do modelo são apresentadas integralmente, sem streaming de tokens.
- A agenda local depende de o servidor continuar ligado.
- Recursos disponíveis variam conforme o modelo NVIDIA escolhido e as permissões dos serviços externos.

## Documentação e imagens

- [Relatório de auditoria técnica](AUDIT.md)
- [Resumo das correções revisadas](REVIEWED_FIXES.md)
- [Capa SVG](public/images/samael-dev-cover.svg)
- [Referência do dashboard SVG](public/images/samael-dev-dashboard.svg)

## Licença

Este projeto é distribuído sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para ver o texto integral da licença, incluindo permissões, condições e isenção de garantia.

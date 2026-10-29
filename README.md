# SAMAEL DEV

**Workspace de engenharia de software com IA, agentes especializados e automação de fluxos.**

![SAMAEL DEV — capa monocromática](public/images/samael-dev-cover.svg)

O **SAMAEL DEV** é um projeto de workspace web voltado ao desenvolvimento de software assistido por inteligência artificial. A proposta combina uma interface responsiva, orquestração de agentes especializados, integração com a API NVIDIA NIM, ferramentas compatíveis com MCP e automações por meio do n8n.

A interface foi planejada para uso em computadores e dispositivos Android por meio de um navegador moderno.

> **Status do repositório:** a versão atualmente publicada contém documentação, relatório de auditoria e referências visuais. Os arquivos executáveis principais, como `server.py`, `public/index.html` e a suíte `tests/`, ainda não estão disponíveis na árvore principal. Portanto, clonar este repositório baixa a documentação e os recursos publicados, mas **não instala uma versão executável do SAMAEL DEV**. Os passos de inicialização da aplicação só poderão ser usados quando o código-fonte correspondente for incluído.

---

## Sumário

- [Visão geral](#visão-geral)
- [Recursos planejados](#recursos-planejados)
- [Arquitetura e tecnologias](#arquitetura-e-tecnologias)
- [Requisitos](#requisitos)
- [Baixar o repositório](#baixar-o-repositório)
- [Instalação no Termux (Android)](#instalação-no-termux-android)
- [Instalação no Windows](#instalação-no-windows)
- [Instalação no Kali Linux](#instalação-no-kali-linux)
- [Configuração da NVIDIA API](#configuração-da-nvidia-api)
- [Instalação do n8n com Docker](#instalação-do-n8n-com-docker)
- [Conectar o SAMAEL DEV ao n8n](#conectar-o-samael-dev-ao-n8n)
- [Segurança](#segurança)
- [Limitações e estado atual](#limitações-e-estado-atual)
- [Documentação e referências visuais](#documentação-e-referências-visuais)
- [Licença](#licença)

## Visão geral

O SAMAEL DEV foi concebido para reunir em um único ambiente as tarefas de programação assistida por IA, a coordenação de agentes especializados e a integração com ferramentas externas. A inferência de IA é realizada por meio da API NVIDIA NIM; o servidor da aplicação, quando disponibilizado, é executado no computador ou servidor escolhido pelo usuário.

O projeto também prevê integração com servidores MCP e com workflows do n8n, permitindo conectar ferramentas e automatizar tarefas de acordo com as permissões configuradas.

## Recursos planejados

| Área | Descrição |
|---|---|
| Workspace de IA | Interface de conversação para descrever tarefas técnicas e orientar o orquestrador. |
| Geração de arquivos | Preparação de arquivos gerados pela IA e empacotamento para download, conforme o código implementado. |
| Entrada multimodal | Tratamento de anexos de imagem, vídeo e texto; o comportamento depende dos recursos implementados e do modelo utilizado. |
| Agentes especializados | Orquestração de até oito agentes, com possibilidade de executar tarefas independentes em paralelo. |
| Dependências de tarefas | Organização de etapas que dependem da conclusão de outras tarefas. |
| Catálogo de Skills | Importação de Skills de repositórios Git ou arquivos `SKILL.md`; revise o conteúdo antes de utilizá-lo. |
| Servidores MCP | Integração planejada com servidores MCP compatíveis, incluindo ferramentas externas autorizadas. |
| Aprovação de ferramentas | Fluxo de confirmação para operações que possam alterar dados ou executar ações sensíveis, conforme a implementação. |
| Integração com n8n | Conexão com workflows e webhooks configurados pelo usuário. |
| Persistência | Armazenamento de configurações e dados operacionais no ambiente de execução, quando disponível. |
| Interface responsiva | Experiência web planejada para navegadores desktop e móveis. |

### Referência visual

![Referência monocromática do dashboard SAMAEL DEV](public/images/samael-dev-dashboard.svg)

As imagens são **ilustrações vetoriais de referência**, não capturas de tela de uma aplicação executável.

## Arquitetura e tecnologias

- **Interface planejada:** HTML, CSS e JavaScript.
- **Servidor planejado:** Python 3.
- **Provedor de IA:** NVIDIA NIM / API compatível com chat completions.
- **Ferramentas externas:** servidores MCP compatíveis.
- **Automação:** n8n por meio de API e webhooks.
- **Endereço local previsto:** `http://127.0.0.1:8000`.

Essas tecnologias descrevem a arquitetura prevista; a presença e o funcionamento de cada recurso dependem da publicação do código-fonte correspondente.

## Requisitos

Para consultar e editar a documentação:

- Git (opcional, para clonar o repositório).
- Um navegador ou editor de texto.

Para executar a aplicação quando o código-fonte estiver disponível:

- Python 3.9 ou superior, conforme os requisitos do código.
- Uma chave NVIDIA API e um identificador de modelo compatível.
- Opcionalmente, uma instância n8n e servidores MCP configurados.
- Para executar o n8n com Docker, Docker Engine e Docker Compose (ou suporte equivalente do Docker Desktop).

## Baixar o repositório

Os comandos abaixo baixam o repositório diretamente do GitHub. Eles **não dependem de um ZIP previamente salvo no celular**.

### Termux, Kali Linux ou outro terminal Linux

```bash
pkg install git -y  # Termux; no Kali/Debian, use: sudo apt install git
git clone https://github.com/stylesxzz/Samael-dev.git
cd Samael-dev
ls -la
```

No Kali Linux ou Debian, caso o Git ainda não esteja instalado:

```bash
sudo apt update
sudo apt install -y git
git clone https://github.com/stylesxzz/Samael-dev.git
cd Samael-dev
```

### Windows PowerShell

```powershell
git --version
git clone https://github.com/stylesxzz/Samael-dev.git
Set-Location Samael-dev
Get-ChildItem
```

Se o comando `git --version` não for reconhecido, instale o Git para Windows e abra um novo PowerShell.

## Instalação no Termux (Android)

1. Instale e abra o Termux.
2. Instale o Git e o Python, caso precise preparar o ambiente para desenvolvimento:

```bash
pkg update
pkg upgrade -y
pkg install -y git python nano
```

3. Clone o repositório e entre na pasta criada pelo Git:

```bash
git clone https://github.com/stylesxzz/Samael-dev.git
cd Samael-dev
ls -la
```

**Importante:** neste momento, o repositório não contém o servidor e a interface executáveis. Por isso, não execute `python server.py` nem espere que o endereço local abra a aplicação antes de o código-fonte ser publicado.

O Termux, por si só, também não oferece um Docker Engine completo pronto para uso. Para executar o n8n com Docker, utilize um computador Linux/Windows com Docker ou um servidor remoto com Docker instalado. Depois, acesse a URL desse servidor a partir do navegador do Android.

## Instalação no Windows

1. Instale o Git para Windows.
2. Instale Python 3.9 ou superior se for preparar um ambiente de desenvolvimento.
3. Abra o PowerShell e clone o repositório:

```powershell
git clone https://github.com/stylesxzz/Samael-dev.git
Set-Location Samael-dev
Get-ChildItem
```

O código executável principal ainda não está publicado. Quando ele estiver disponível, siga os requisitos e o comando de inicialização documentados para essa versão. Para executar o n8n localmente com Docker, instale o Docker Desktop e habilite o backend WSL 2, se aplicável.

## Instalação no Kali Linux

Instale as ferramentas básicas e clone o projeto:

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
git clone https://github.com/stylesxzz/Samael-dev.git
cd Samael-dev
ls -la
```

Esses passos preparam o ambiente e baixam os arquivos publicados. A aplicação SAMAEL DEV não poderá ser iniciada até que o código-fonte executável seja adicionado ao repositório.

## Configuração da NVIDIA API

Quando o código da aplicação estiver disponível, a integração deverá utilizar uma chave válida e um identificador de modelo habilitado para a sua conta NVIDIA. O formato de configuração previsto é:

```dotenv
NVIDIA_API_KEY=COLOQUE_SUA_CHAVE_AQUI
NVIDIA_MODEL=ID_EXATO_DO_MODELO
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
```

Os nomes acima representam as variáveis previstas na documentação; confirme que correspondem ao código da versão instalada antes de utilizá-las. A disponibilidade de modelos, limites e condições de uso é definida pela NVIDIA.

**Nunca** inclua chaves reais no README, em commits, capturas de tela ou registros públicos.

## Instalação do n8n com Docker

Esta seção instala o n8n separadamente do SAMAEL DEV. O Docker deve estar instalado e em execução na máquina ou servidor escolhido. Consulte a [documentação oficial do Docker](https://docs.docker.com/get-started/get-docker/) para instalar o mecanismo adequado ao seu sistema.

### 1. Entrar na conta Docker Hub

No terminal, execute:

```bash
docker login
```

O Docker Hub normalmente oferece um fluxo de autenticação pelo navegador e um código temporário. Abra o endereço indicado pelo terminal, entre na sua conta Docker e confirme o código. Não compartilhe esse código com outras pessoas.

Verifique se o Docker está disponível:

```bash
docker --version
docker compose version
```

Se o comando `docker` não existir ou o daemon não estiver ativo, conclua a instalação e inicie o Docker antes de continuar. Fazer login não instala o Docker Engine.

### 2. Baixar a imagem oficial do n8n

```bash
docker pull n8nio/n8n
```

### 3. Criar um volume persistente

O volume mantém os dados do n8n entre reinicializações e recriações do contêiner.

```bash
docker volume create n8n_data
```

### 4. Iniciar o n8n

```bash
docker run -d \
  --name n8n \
  --restart unless-stopped \
  -p 127.0.0.1:5678:5678 \
  -e GENERIC_TIMEZONE=America/Sao_Paulo \
  -e TZ=America/Sao_Paulo \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```

Abra no navegador da própria máquina:

```text
http://localhost:5678
```

Siga a tela inicial do n8n para criar a conta de proprietário e configurar o acesso. O mapeamento da porta para `127.0.0.1` limita o acesso ao próprio computador; é uma opção mais segura para uso local.

### 5. Verificar o contêiner

```bash
docker ps
docker logs -f n8n
```

Para sair da visualização dos logs, pressione `Ctrl+C`. Isso não interrompe o contêiner.

### 6. Comandos úteis para administrar o n8n

```bash
# Parar
docker stop n8n

# Iniciar novamente
docker start n8n

# Reiniciar
docker restart n8n

# Ver logs recentes
docker logs --tail 100 n8n

# Atualizar a imagem
docker pull n8nio/n8n
docker stop n8n
docker rm n8n
docker run -d \
  --name n8n \
  --restart unless-stopped \
  -p 127.0.0.1:5678:5678 \
  -e GENERIC_TIMEZONE=America/Sao_Paulo \
  -e TZ=America/Sao_Paulo \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```

O comando de atualização recria o contêiner, mas preserva o volume `n8n_data`. Antes de atualizar uma instância importante, faça backup dos dados e confira as notas de versão do n8n.

### Observações sobre acesso remoto

- Em um servidor remoto, `localhost` no navegador do celular aponta para o próprio celular, não para o servidor.
- Para acessar uma instância remota, configure um domínio ou endereço do servidor e uma conexão protegida por HTTPS, autenticação e firewall.
- Não exponha a porta 5678 diretamente à internet sem controles de segurança.
- O login do Docker Hub autentica o cliente no registro de imagens; ele não configura, por si só, o acesso remoto ao n8n.

Consulte também a [documentação oficial do n8n para Docker](https://docs.n8n.io/hosting/installation/docker/).

## Conectar o SAMAEL DEV ao n8n

A integração depende de o código executável do SAMAEL DEV ser publicado e de a versão implementada oferecer suporte às variáveis e chamadas necessárias. O formato previsto na documentação é:

```dotenv
N8N_URL=http://localhost:5678
N8N_API_KEY=COLOQUE_SUA_CHAVE_N8N_AQUI
```

Esses valores são exemplos, não uma garantia de que a integração já esteja operacional no repositório atual.

Para configurar a integração quando o recurso estiver disponível:

1. Inicie o n8n e entre na interface web.
2. Crie um workflow e configure o gatilho ou webhook necessário.
3. Ative o workflow e teste a URL do webhook.
4. Crie uma chave de API nas configurações do n8n, se a integração utilizar a API autenticada.
5. Configure a URL e a credencial no ambiente do SAMAEL DEV, sem publicá-las no Git.
6. Teste primeiro com uma automação não destrutiva.

Se o SAMAEL DEV estiver em outro contêiner, `localhost:5678` geralmente não apontará para o contêiner do n8n. Nesse caso, configure ambos na mesma rede Docker e use o nome do serviço/contêiner como hostname, ou utilize o endereço correto do servidor. Não use a URL de loopback sem confirmar onde cada processo está executando.

## Segurança

- Mantenha arquivos de segredos, como `.env`, fora do controle de versão.
- Não compartilhe chaves NVIDIA, tokens de API, códigos temporários de login ou credenciais OAuth.
- Prefira credenciais com privilégios mínimos e revogue as que não forem mais necessárias.
- Revise Skills e ferramentas MCP de terceiros antes de habilitá-las.
- Exija aprovação para operações que alterem arquivos, dados ou sistemas.
- Antes de disponibilizar serviços na rede, configure HTTPS, autenticação, firewall e regras de acesso.
- Faça backups regulares dos volumes e dados persistentes do n8n.

## Limitações e estado atual

- O repositório público ainda não inclui os arquivos executáveis principais da aplicação.
- As imagens publicadas são referências visuais, não capturas de tela reais.
- Os recursos descritos como planejados dependem da publicação e validação do código correspondente.
- A integração com n8n requer uma instância funcional e workflows configurados.
- Os recursos disponíveis pela API dependem do modelo NVIDIA e das permissões da conta.

## Documentação e referências visuais

- [Relatório de auditoria técnica](AUDIT.md)
- [Resumo das correções revisadas](REVIEWED_FIXES.md)
- [Capa SVG](public/images/samael-dev-cover.svg)
- [Referência do dashboard SVG](public/images/samael-dev-dashboard.svg)
- [Documentação oficial do Docker](https://docs.docker.com/)
- [Documentação oficial do n8n](https://docs.n8n.io/)

## Licença

Este projeto é distribuído sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para ler os termos completos, incluindo permissões, condições e isenção de garantia.

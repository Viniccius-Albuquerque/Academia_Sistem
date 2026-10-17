# Sistema de Gerenciamento de Academia

Sistema de gerenciamento de academia desenvolvido em Python, com uma API REST construída com FastAPI, banco de dados PostgreSQL e interface web em HTML, CSS e JavaScript.

O projeto permite gerenciar alunos, treinos e exercícios, integrando o front-end ao back-end por meio de requisições HTTP.

O objetivo é praticar conceitos de desenvolvimento web, Programação Orientada a Objetos (POO), organização em camadas, operações SQL, validação de dados e integração entre aplicações.

## Tecnologias utilizadas

### Back-end
- **Python** — linguagem principal.
- **FastAPI** — desenvolvimento da API REST.
- **Pydantic** — validação dos dados de entrada e estruturação das respostas.
- **PostgreSQL** — banco de dados relacional.
- **Psycopg** — conexão e execução de comandos SQL.
- **python-dotenv** — carregamento das configurações a partir de variáveis de ambiente.
- **Uvicorn** — servidor ASGI utilizado para executar a aplicação.

### Front-end
- **HTML5** — estrutura das páginas.
- **CSS3** — estilização e responsividade.
- **JavaScript** — lógica da interface e comunicação com a API.
- **Fetch API** — envio de requisições HTTP ao back-end.

### Ferramentas
- Git e GitHub para versionamento do código.
- Visual Studio Code para desenvolvimento.

## Funcionalidades

### Alunos
- Cadastrar alunos.
- Listar todos os alunos cadastrados.
- Buscar aluno por ID.
- Buscar alunos por plano.
- Atualizar idade e plano.
- Ativar e desativar alunos.
- Excluir alunos.
- Visualizar indicadores de quantidade de alunos ativos e inativos.

Os planos disponíveis são `basico`, `intermediario` e `pro`.

### Treinos
- Cadastrar treinos vinculados a alunos.
- Consultar os treinos de um aluno.
- Atualizar o nome de um treino utilizando o aluno e o dia da semana.
- Excluir treinos.
- Excluir exercícios associados aos treinos removidos, conforme a lógica implementada no serviço.

Os dias da semana aceitos pelo serviço são `segunda`, `terca`, `quarta`, `quinta`, `sexta`, `sabado` e `domingo`.

### Exercícios
- Cadastrar exercícios vinculados a treinos.
- Consultar os exercícios de um treino.
- Atualizar nome, séries e repetições.
- Excluir exercícios.

Cada exercício possui nome, quantidade de séries, quantidade de repetições e vínculo com um treino.

## Interface web

A interface foi desenvolvida com HTML, CSS e JavaScript puro, sem depender de um framework de front-end.

O painel está dividido em três módulos principais:
- **Alunos:** cadastro, listagem, busca por ID, busca por plano e gerenciamento dos registros.
- **Treinos:** cadastro, consulta, atualização e exclusão.
- **Exercícios:** cadastro, consulta, atualização e exclusão.

A comunicação entre a interface e a API é centralizada em `frontend/js/api.js`. Os demais arquivos JavaScript são separados por módulo, facilitando a manutenção do código.

## Estrutura do projeto

```text
Academia_Sistem/
├── database/
│   └── conexao.py
│
├── modules/
│   ├── aluno.py
│   ├── treino.py
│   └── exercicio.py
│
├── repositories/
│   ├── aluno_repository.py
│   ├── treino_repository.py
│   └── exercicio_repository.py
│
├── routes/
│   ├── aluno_routes.py
│   ├── treino_routes.py
│   └── exercicio_routes.py
│
├── schemas/
│   ├── aluno_schema.py
│   ├── treino_schemas.py
│   └── exercicio_schema.py
│
├── services/
│   ├── aluno_service.py
│   ├── treino_service.py
│   └── exercicio_service.py
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── api.js
│       ├── alunos.js
│       ├── treinos.js
│       └── exercicios.js
│
├── .env.example
├── .gitignore
├── main.py
└── README.MD
```

### Organização do back-end

- **`modules/`** — classes e regras de validação das entidades do sistema.
- **`schemas/`** — modelos Pydantic utilizados nas requisições e respostas da API.
- **`repositories/`** — operações SQL e comunicação direta com o banco de dados.
- **`services/`** — regras de negócio e coordenação das operações.
- **`routes/`** — definição dos endpoints HTTP.
- **`database/`** — configuração da conexão com o PostgreSQL.
- **`main.py`** — inicialização do FastAPI, registro das rotas e menu interativo de terminal.

### Organização do front-end

- **`frontend/index.html`** — estrutura do painel de gerenciamento.
- **`frontend/css/style.css`** — estilos e adaptação para diferentes tamanhos de tela.
- **`frontend/js/api.js`** — requisições HTTP, tratamento de respostas e funções compartilhadas.
- **`frontend/js/alunos.js`** — operações relacionadas aos alunos.
- **`frontend/js/treinos.js`** — operações relacionadas aos treinos.
- **`frontend/js/exercicios.js`** — operações relacionadas aos exercícios.

## Banco de dados

O projeto utiliza PostgreSQL para persistência dos dados.

A estrutura principal relaciona três entidades:

```text
Aluno
  |
  └── Treino
        |
        └── Exercício
```

Um aluno pode possuir treinos, e cada treino pode possuir exercícios. Os relacionamentos são realizados por meio dos identificadores dos registros.

As configurações de conexão são carregadas a partir de variáveis de ambiente, evitando deixar as credenciais diretamente no código-fonte.

**Observação:** o banco de dados e as tabelas precisam estar criados e configurados antes de executar a aplicação. Consulte os arquivos do projeto para verificar a estrutura SQL esperada.

## API REST

A API utiliza FastAPI e organiza os endpoints por recurso.

A documentação interativa é gerada automaticamente pelo FastAPI.

### Alunos

Prefixo: `/alunos`

| Método | Endpoint | Operação |
|---|---|---|
| `POST` | `/alunos/` | Cadastrar aluno |
| `GET` | `/alunos/` | Listar alunos |
| `GET` | `/alunos/id/{id}` | Buscar aluno por ID |
| `GET` | `/alunos/plano/{plano}` | Buscar alunos por plano |
| `PATCH` | `/alunos/{id}` | Atualizar idade e plano |
| `PATCH` | `/alunos/ativar/{id}` | Ativar aluno |
| `PATCH` | `/alunos/desativar/{id}` | Desativar aluno |
| `DELETE` | `/alunos/{id}` | Excluir aluno |

Valores aceitos para `plano`: `basico`, `intermediario` e `pro`.

### Treinos

Prefixo: `/treino`

| Método | Endpoint | Operação |
|---|---|---|
| `POST` | `/treino/` | Cadastrar treino |
| `GET` | `/treino/{id_aluno}` | Consultar treinos de um aluno |
| `PUT` | `/treino/{id_aluno}` | Atualizar o nome de um treino |
| `DELETE` | `/treino/delete` | Excluir treino pelo aluno e dia da semana |

A atualização e a exclusão utilizam o ID do aluno e o dia da semana como critérios. A exclusão pode afetar os exercícios associados aos treinos removidos.

### Exercícios

Prefixo: `/exercicio`

| Método | Endpoint | Operação |
|---|---|---|
| `POST` | `/exercicio/` | Cadastrar exercício |
| `GET` | `/exercicio/{id_treino}` | Consultar exercícios de um treino |
| `PUT` | `/exercicio/atualizar/{id}` | Atualizar exercício |
| `DELETE` | `/exercicio/delete/{id}` | Excluir exercício |

## Como executar o projeto localmente

### 1. Pré-requisitos

- Python instalado.
- PostgreSQL instalado e em execução.
- Banco de dados e tabelas configurados.
- Visual Studio Code.
- Extensão Live Server do VS Code para abrir o front-end.

### 2. Clonar o repositório

```bash
git clone https://github.com/Viniccius-Albuquerque/Academia_Sistem.git
cd Academia_Sistem
```

### 3. Criar e ativar o ambiente virtual

No Windows, utilizando PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências do back-end

```bash
python -m pip install fastapi "uvicorn[standard]" "psycopg[binary]" python-dotenv
```

### 5. Configurar as variáveis de ambiente

Na raiz do projeto, copie o arquivo de exemplo:

```powershell
Copy-Item .env.example .env
```

Edite o arquivo `.env` com as configurações do seu PostgreSQL:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui
```

Substitua os valores de exemplo pelas configurações da sua instalação.

**Importante:** não compartilhe o arquivo `.env` nem envie credenciais reais ao GitHub. O `.gitignore` já está configurado para ignorá-lo.

### 6. Iniciar o back-end

Com o PostgreSQL em execução, o ambiente virtual ativado e as configurações preenchidas, execute na raiz do projeto:

```bash
uvicorn main:app --reload
```

A API estará disponível em:

- API: http://127.0.0.1:8000
- Documentação interativa: http://127.0.0.1:8000/docs
- Documentação alternativa: http://127.0.0.1:8000/redoc

Acesse `/docs` para consultar os endpoints e testar as requisições diretamente pelo navegador.

### 7. Iniciar o front-end

Com o back-end em execução:

1. Abra a pasta do projeto no VS Code.
2. Abra `frontend/index.html`.
3. Clique com o botão direito no arquivo.
4. Selecione **Open with Live Server**.

Normalmente, o Live Server disponibiliza a interface em:

```text
http://127.0.0.1:5500
```

O front-end está configurado para enviar requisições à API em `http://127.0.0.1:8000`.

O CORS está configurado no `main.py` para permitir as origens locais `http://127.0.0.1:5500` e `http://localhost:5500`. Se o Live Server utilizar outra porta, será necessário ajustar essa configuração.

### 8. Executar o menu de terminal

O projeto também mantém uma interface interativa no terminal. Para executá-la:

```bash
python main.py
```

## Deploy

O projeto foi desenvolvido e testado em ambiente local. O deploy ainda não faz parte da versão atual.

Uma etapa futura de aprendizado será estudar como publicar temporariamente o front-end, o back-end e o banco de dados em serviços de hospedagem, incluindo as configurações de ambiente, conexão entre serviços, CORS e diferenças entre desenvolvimento local e produção.

## Próximos passos

- [x] Desenvolver as classes e entidades do sistema.
- [x] Implementar operações com PostgreSQL.
- [x] Organizar o back-end em repositories, services e routes.
- [x] Criar schemas com Pydantic.
- [x] Desenvolver os endpoints com FastAPI.
- [x] Implementar a interface web com HTML, CSS e JavaScript.
- [x] Integrar o front-end ao back-end por meio da API REST.
- [x] Implementar as operações de alunos, treinos e exercícios na interface.
- [ ] Estudar e realizar um deploy experimental gratuito.
- [ ] Avaliar melhorias futuras na interface, validação e tratamento de erros.

## Objetivo do projeto

Consolidar conhecimentos de Python, Programação Orientada a Objetos, SQL, PostgreSQL, APIs REST, organização em camadas e integração entre front-end e back-end.

O projeto representa uma aplicação prática de aprendizado, desenvolvida de forma incremental para aprofundar os conhecimentos em desenvolvimento web.

# Academia Sistem

Sistema web para gerenciamento de academia, desenvolvido com Python, FastAPI e PostgreSQL. A aplicação permite gerenciar alunos, treinos e exercícios por meio de uma interface web integrada a uma API REST.

## Aplicação online

- **Aplicação web:** [Acessar Academia Sistem](https://academiasistem.netlify.app)
- **Documentação da API:** [FastAPI — Swagger UI](https://academia-sistem.onrender.com/docs)
- **Código-fonte:** [GitHub — Academia_Sistem](https://github.com/Viniccius-Albuquerque/Academia_Sistem)

> A aplicação utiliza serviços de hospedagem com planos gratuitos. A API pode apresentar demora na primeira requisição após períodos de inatividade.

## Funcionalidades

### Gerenciamento de alunos
- Cadastro e listagem de alunos.
- Consulta por identificador e busca por plano.
- Atualização de informações.
- Ativação e desativação de cadastros.
- Exclusão de alunos.

### Gerenciamento de treinos
- Cadastro de treinos vinculados a alunos.
- Consulta dos treinos de um aluno.
- Atualização e exclusão de treinos.

### Gerenciamento de exercícios
- Cadastro de exercícios vinculados a treinos.
- Consulta dos exercícios de um treino.
- Atualização e exclusão de exercícios.

## Tecnologias utilizadas

- **Python** — desenvolvimento do backend.
- **FastAPI** — construção da API REST.
- **Pydantic** — validação e estruturação dos dados.
- **PostgreSQL** — banco de dados relacional.
- **Psycopg** — conexão com o banco de dados.
- **HTML, CSS e JavaScript** — desenvolvimento do frontend.
- **Neon** — hospedagem do banco de dados.
- **Render** — hospedagem do backend.
- **Netlify** — hospedagem do frontend.

## Arquitetura do projeto

O backend está organizado em camadas para separar as responsabilidades:

- **Routes:** recebem e encaminham as requisições HTTP.
- **Services:** concentram as regras de negócio.
- **Repositories:** realizam as operações de acesso aos dados.
- **Modules e Schemas:** organizam os objetos e estruturas utilizados pela aplicação.
- **Database:** configura a conexão com o PostgreSQL.

O frontend consome a API e apresenta os recursos de gerenciamento por meio de uma interface web.

## Estrutura de pastas

```text
Academia_Sistem/
├── database/
│   └── conexao.py
├── frontend/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── api.js
│   │   ├── alunos.js
│   │   ├── treinos.js
│   │   └── exercicios.js
│   └── index.html
├── modules/
├── repositories/
├── routes/
├── schemas/
├── services/
├── main.py
├── requirements.txt
└── .env.example
```

## Executar localmente

### 1. Pré-requisitos

- Python instalado.
- PostgreSQL acessível.
- Git.

### 2. Clonar o repositório

```bash
git clone https://github.com/Viniccius-Albuquerque/Academia_Sistem.git
cd Academia_Sistem
```

### 3. Criar e ativar um ambiente virtual

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, usando `.env.example` como referência:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui
```

Substitua os valores pelos dados do seu banco PostgreSQL. Não publique credenciais reais no GitHub.

O banco precisa ter as tabelas `aluno`, `treino` e `exercicio`, com as colunas esperadas pelo código. Os treinos são associados aos alunos por `id_aluno`, e os exercícios são associados aos treinos por `id_treino`.

**Importante:** os scripts SQL para criação das tabelas não estão incluídos no repositório. É necessário preparar o esquema do banco antes de iniciar a aplicação.

### 6. Iniciar o backend

Na raiz do projeto, execute:

```bash
uvicorn main:app --reload
```

A API ficará disponível em `http://127.0.0.1:8000`.

A documentação interativa poderá ser acessada em `http://127.0.0.1:8000/docs`.

### 7. Executar o frontend localmente

Abra `frontend/index.html` por meio de um servidor estático, como a extensão Live Server do VS Code.

Para desenvolvimento local, confira se a variável `API_URL`, no arquivo `frontend/js/api.js`, aponta para:

```javascript
const API_URL = "http://127.0.0.1:8000";
```

A origem local também precisa estar autorizada na configuração de CORS do backend. Para utilizar a aplicação publicada, mantenha a URL pública do Render configurada no frontend.

## Principais endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/alunos/` | Listar alunos |
| POST | `/alunos/` | Cadastrar aluno |
| GET | `/alunos/id/{id}` | Consultar aluno por ID |
| PATCH | `/alunos/{id}` | Atualizar dados do aluno |
| DELETE | `/alunos/{id}` | Excluir aluno |
| PATCH | `/alunos/ativar/{id}` | Ativar aluno |
| PATCH | `/alunos/desativar/{id}` | Desativar aluno |
| GET | `/alunos/plano/{plano}` | Buscar alunos por plano |
| POST | `/treino/` | Cadastrar treino |
| GET | `/treino/{id_aluno}` | Listar treinos de um aluno |
| PUT | `/treino/{id_aluno}` | Atualizar treino |
| DELETE | `/treino/delete` | Excluir treino |
| POST | `/exercicio/` | Cadastrar exercício |
| GET | `/exercicio/{id_treino}` | Listar exercícios de um treino |
| PUT | `/exercicio/atualizar/{id}` | Atualizar exercício |
| DELETE | `/exercicio/delete/{id}` | Excluir exercício |

Para consultar os parâmetros, os formatos das requisições e as respostas, acesse a [documentação interativa da API](https://academia-sistem.onrender.com/docs).

## Objetivo do projeto

Projeto de estudo e prática de desenvolvimento backend, integração com banco de dados relacional, organização de código em camadas e construção de uma interface web que consome uma API REST.

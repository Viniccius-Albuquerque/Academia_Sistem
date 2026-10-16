# Sistema de Gerenciamento de Academia

Projeto desenvolvido em Python para praticar desenvolvimento backend, Programação Orientada a Objetos (POO), SQL, PostgreSQL e construção de APIs REST.

O sistema permite gerenciar alunos, treinos e exercícios de uma academia. Atualmente, possui uma API desenvolvida com FastAPI e um menu interativo executado pelo terminal.

O projeto está em desenvolvimento incremental, com foco no aprendizado prático dos conceitos de backend.

## Tecnologias utilizadas

- **Python** — linguagem principal.
- **FastAPI** — criação da API REST.
- **Pydantic** — validação dos dados recebidos pela API.
- **PostgreSQL** — banco de dados relacional.
- **Psycopg** — conexão e execução de comandos SQL no PostgreSQL.
- **SQL** — consultas e operações no banco de dados.
- **Programação Orientada a Objetos (POO)** — classes, entidades, propriedades e herança.
- **python-dotenv** — carregamento das configurações a partir de variáveis de ambiente.
- **Git e GitHub** — versionamento do código.

## Funcionalidades

### Alunos

- Cadastrar alunos.
- Listar alunos cadastrados.
- Buscar aluno por ID.
- Buscar alunos por plano.
- Atualizar idade e plano.
- Ativar e desativar alunos.
- Excluir alunos.

Os planos disponíveis são `basico`, `intermediario` e `pro`. O sistema também trabalha com o estado do aluno, permitindo marcá-lo como ativo ou desativado.

### Treinos

- Cadastrar treinos vinculados a alunos.
- Consultar os treinos de um aluno.
- Atualizar informações de um treino.
- Excluir treinos.

Os treinos possuem nome, dia da semana e vínculo com o aluno.

### Exercícios

- Cadastrar exercícios vinculados a treinos.
- Consultar os exercícios de um treino.
- Atualizar nome, séries e repetições.
- Excluir exercícios.

Cada exercício possui nome, quantidade de séries, quantidade de repetições e vínculo com um treino.

## Arquitetura do projeto

O código está organizado em camadas, separando as principais responsabilidades da aplicação.

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
├── .env.example
├── .gitignore
├── main.py
└── README.MD
```

### Responsabilidade de cada camada

- **`modules/`** — contém as classes que representam alunos, treinos e exercícios, incluindo validações feitas por propriedades e setters.
- **`schemas/`** — define os modelos Pydantic utilizados para validar os dados de entrada e estruturar as respostas da API.
- **`repositories/`** — contém as operações SQL e a comunicação direta com o PostgreSQL.
- **`services/`** — coordena as operações e aplica regras de negócio.
- **`routes/`** — define os endpoints da API, recebe as requisições HTTP e retorna as respostas.
- **`database/`** — centraliza a configuração da conexão com o banco de dados.
- **`main.py`** — inicializa a aplicação FastAPI, registra os routers e mantém o menu interativo do terminal.

## Banco de dados

O projeto utiliza PostgreSQL para armazenar os dados.

A estrutura trabalha com três entidades principais:

```text
aluno
  │
  └── treino
         │
         └── exercicio
```

Os treinos estão associados a alunos, e os exercícios estão associados a treinos. Esses vínculos são representados pelos identificadores utilizados nas tabelas.

A aplicação executa operações SQL por meio do Psycopg, utilizando parâmetros nas consultas para fornecer os valores recebidos pelas funções.

## API REST

A API é desenvolvida com FastAPI e utiliza schemas Pydantic para validar os dados recebidos. Os endpoints estão organizados por recurso.

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

### Treinos

Prefixo: `/treino`

| Método | Endpoint | Operação |
|---|---|---|
| `POST` | `/treino/` | Cadastrar treino |
| `GET` | `/treino/{id_aluno}` | Consultar treinos de um aluno |
| `PUT` | `/treino/{id_aluno}` | Atualizar treino |
| `DELETE` | `/treino/delete` | Excluir treino |

A exclusão de treino recebe um corpo JSON com o dia da semana e o ID do aluno.

### Exercícios

Prefixo: `/exercicio`

| Método | Endpoint | Operação |
|---|---|---|
| `POST` | `/exercicio/` | Cadastrar exercício |
| `GET` | `/exercicio/{id_treino}` | Consultar exercícios de um treino |
| `PUT` | `/exercicio/atualizar/{id}` | Atualizar exercício |
| `DELETE` | `/exercicio/delete/{id}` | Excluir exercício |

## Executando o projeto

### 1. Pré-requisitos

- Python instalado.
- PostgreSQL instalado e em execução.
- Banco de dados criado e tabelas configuradas conforme a estrutura utilizada pelo projeto.

### 2. Clonar o repositório

```bash
git clone https://github.com/Viniccius-Albuquerque/Academia_Sistem.git
cd Academia_Sistem
```

### 3. Criar e ativar um ambiente virtual

No Windows, utilizando PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
python -m pip install fastapi "uvicorn[standard]" "psycopg[binary]" python-dotenv
```

### 5. Configurar o banco de dados

Copie o arquivo de exemplo para criar o arquivo de configuração local.

No PowerShell:

```powershell
Copy-Item .env.example .env
```

Edite o `.env` com os dados da sua instalação do PostgreSQL:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui
```

Substitua os valores de exemplo pelas configurações reais do seu banco de dados.

O arquivo `.env` contém configurações locais e não deve ser enviado ao GitHub.

### 6. Executar a API

Com o ambiente virtual ativado e o banco configurado, execute:

```bash
uvicorn main:app --reload
```

Por padrão, a aplicação estará disponível em:

- API: http://127.0.0.1:8000
- Documentação interativa: http://127.0.0.1:8000/docs
- Documentação alternativa: http://127.0.0.1:8000/redoc

A documentação interativa permite visualizar os endpoints, enviar requisições e consultar as respostas da API pelo navegador.

### Menu de terminal

O projeto também mantém um menu interativo para gerenciar alunos, treinos e exercícios pelo terminal:

```bash
python main.py
```

## Próximos passos

- [x] Desenvolver as classes e entidades do sistema.
- [x] Implementar operações com PostgreSQL.
- [x] Organizar o código em repositories e services.
- [x] Criar schemas com Pydantic.
- [x] Desenvolver endpoints com FastAPI.
- [x] Integrar os routers à aplicação principal.
- [ ] Desenvolver o frontend da aplicação.
- [ ] Conectar o frontend ao backend por meio da API REST.
- [ ] Integrar as operações de alunos, treinos e exercícios à interface.

## Objetivo do projeto

Consolidar conhecimentos de Python, POO, SQL, PostgreSQL, separação de responsabilidades, validação de dados, construção de APIs REST e integração entre frontend e backend.

O projeto representa uma etapa prática de aprendizado e será utilizado como base para desenvolver a interface e ampliar a experiência com aplicações web completas.
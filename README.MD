# Sistema de Gerenciamento de Academia

Projeto desenvolvido em Python para estudo de desenvolvimento backend, utilizando PostgreSQL e uma arquitetura separada em entidades, serviços e repositórios.

O sistema permite o gerenciamento de alunos, treinos e exercícios de uma academia.

> Projeto desenvolvido com foco em aprendizado e evolução gradual para uma API REST utilizando FastAPI.

## Tecnologias utilizadas

- Python
- PostgreSQL
- psycopg
- POO
- SQL
- Git e GitHub

## Funcionalidades atuais

### Alunos

- Cadastrar aluno
- Listar alunos
- Buscar aluno por ID
- Buscar alunos por plano
- Atualizar aluno
- Desativar aluno
- Ativar aluno
- Deletar aluno

### Treinos

- Cadastrar treino
- Listar treinos de um aluno
- Atualizar treino
- Deletar treino

### Exercícios

- Cadastrar exercício
- Listar exercícios de um treino
- Atualizar exercício
- Deletar exercício

## Arquitetura

O projeto está sendo desenvolvido utilizando uma separação de responsabilidades:

```text
Aplicação
   │
   ├── Models
   │      └── Entidades do sistema
   │
   ├── Services
   │      └── Regras de negócio
   │
   ├── Repositories
   │      └── Comunicação com o banco de dados
   │
   └── PostgreSQL
          └── Persistência dos dados
```

A estrutura está sendo aprimorada gradualmente conforme novos conceitos de backend são estudados.

## Estrutura planejada

```text
projeto/
├── main.py
├── conexao.py
│
├── models/
│   ├── aluno.py
│   ├── treino.py
│   └── exercicio.py
│
├── schemas/
│
├── services/
│   ├── aluno_service.py
│   ├── treino_service.py
│   └── exercicio_service.py
│
├── repositories/
│   ├── aluno_repository.py
│   ├── treino_repository.py
│   └── exercicio_repository.py
│
└── tests/
```

## Banco de dados

O projeto utiliza PostgreSQL.

As tabelas principais são:

```text
aluno
  │
  └── treino
         │
         └── exercicio
```

Os relacionamentos são realizados através de chaves estrangeiras.

As regras de integridade do banco, como valores permitidos para determinados campos e relacionamentos entre tabelas, são mantidas no próprio PostgreSQL.

## Tratamento de dados

As entidades possuem validações básicas utilizando propriedades e setters.

Exemplo:

```python
@property
def idade(self):
    return self._idade

@idade.setter
def idade(self, nova_idade):
    if not isinstance(nova_idade, int):
        raise ValueError("Idade inválida")

    if nova_idade <= 0:
        raise ValueError("Idade deve ser maior que zero")

    self._idade = nova_idade
```

A validação será posteriormente complementada pela camada de serviços e pelos schemas da API.

## Próximos passos

O projeto está sendo desenvolvido de forma incremental.

Próximas etapas planejadas:

- [ ] Melhorar tratamento de exceções
- [ ] Melhorar validações na camada de serviço
- [ ] Separar Models e Schemas
- [ ] Criar schemas com Pydantic
- [ ] Transformar o sistema em uma API REST
- [ ] Utilizar FastAPI
- [ ] Implementar códigos HTTP adequados
- [ ] Criar documentação automática da API
- [ ] Criar testes automatizados
- [ ] Melhorar gerenciamento das conexões com o banco
- [ ] Utilizar variáveis de ambiente para configurações sensíveis
- [ ] Melhorar arquitetura do projeto
- [ ] Dockerizar a aplicação
- [ ] Realizar deploy

## Objetivo

O objetivo principal deste projeto é consolidar conhecimentos de:

- Python
- Programação Orientada a Objetos
- SQL
- PostgreSQL
- Arquitetura de aplicações
- APIs REST
- FastAPI
- Testes automatizados
- Boas práticas de desenvolvimento backend

O projeto será evoluído continuamente conforme novos conceitos forem estudados.
```
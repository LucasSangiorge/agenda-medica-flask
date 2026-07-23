# Agenda Médica

Projeto feito em Flask para o teste técnico de estágio da TimeSaver. É um sistema simples de agendamentos médicos, com tela de login e uma tabela com os agendamentos vindos de uma API mockada.

## O que tem no projeto

- Login com sessão (verifica usuário e senha no banco SQLite)
- Tela com os agendamentos em tabela (Tabulator.js), com busca por paciente, CPF e médico
- Busca dos agendamentos através de uma API mockada (usando `requests`)
- Tratamento pros principais erros: login errado, API fora do ar, resposta vazia ou inválida, erro no banco, campos faltando
- Logs de erro salvos em `app.log`

## Tecnologias usadas

- Python / Flask
- SQLite
- Tabulator.js
- Docker e Docker Compose

## Como rodar com Docker

Precisa ter o Docker Desktop instalado e aberto.

1. Clonar o repositório:
   ```
   git clone <https://github.com/LucasSangiorge/agenda-medica-flask>
   cd agenda-medica-flask
   ```

2. Criar o arquivo `.env` a partir do `.env.example`:
   ```
   cp .env.example .env
   ```

3. Subir o projeto:
   ```
   docker compose up --build
   ```

4. Abrir no navegador: http://localhost:5000

Na primeira vez que sobe, o banco já é criado e populado com dados de teste automaticamente.

Pra parar: `docker compose down`

## Como rodar sem Docker

Precisa ter Python instalado.

1. Clonar o repositório e entrar na pasta:
   ```
   git clone <url-do-repositorio>
   cd agenda-medica-flask
   ```

2. Criar e ativar o ambiente virtual:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Linux/Mac
   ```

3. Instalar as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Criar o arquivo `.env` a partir do `.env.example`:
   ```
   cp .env.example .env
   ```

5. Popular o banco com os dados de teste:
   ```
   python seed.py
   ```

6. Rodar a aplicação:
   ```
   python run.py
   ```

7. Abrir no navegador: http://localhost:5000

## Login de teste

- E-mail: teste@email.com
- Senha: 123456

## Estrutura das pastas

```
app/
  routes/
    auth.py      # login e logout
    agenda.py    # página da agenda e API mockada
  database.py    # conexão com o SQLite
  __init__.py    # criação da aplicação Flask
config.py        # configurações
seed.py          # cria as tabelas e os dados de teste
run.py           # arquivo que inicia a aplicação
Dockerfile
docker-compose.yml
```

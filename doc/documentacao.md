# Agenda Médica

## Informações do Projeto

- Projeto: Agenda Médica
- Versão: 1.0.0
- Status: 🟡 Em desenvolvimento
- Desenvolvedor: Lucas Sangiorge

---

# Objetivo

Desenvolver uma aplicação web utilizando Flask para gerenciamento e visualização de agendamentos médicos, atendendo aos requisitos propostos no desafio técnico.

---

# Tecnologias

- Python
- Flask
- SQLite
- Requests
- Tabulator
- HTML5
- CSS3
- JavaScript
- Docker
- Git

---

# Arquitetura

## Estrutura de pastas

```
agenda-medica-flask/
├── app/
│   ├── __init__.py        # create_app() - fábrica da aplicação Flask
│   ├── database.py        # conexão com o SQLite
│   └── routes/
│       └── main.py        # rotas (login, agenda, api mock)
├── run.py                 # ponto de entrada, sobe o servidor Flask
├── seed.py                # script manual para criar/popular o banco
├── config.py              # leitura das variáveis de ambiente
├── .env                   # valores reais das variáveis (fora do Git)
├── .env.example            # modelo das variáveis (dentro do Git)
├── requirements.txt
├── Dockerfile              # (Sprint 7)
└── docker-compose.yml      # (Sprint 7)
```

## Decisões técnicas

- **SQLite puro (`sqlite3`), sem ORM**: o escopo do projeto é pequeno (uma tabela de usuários + dados de agendamento), não justifica a complexidade de um SQLAlchemy.
- **Autenticação via `flask.session`**: cookie de sessão assinado nativamente pelo Flask (usando `SECRET_KEY`), sem biblioteca extra como Flask-Login.
- **Senhas com hash (`werkzeug.security`)**: nunca armazenadas em texto puro no banco.
- **API mockada como rota separada dentro do mesmo app** (`/api/agendamentos`), chamada via `requests` a partir da rota da agenda — cumpre o requisito de "requisição HTTP" sem precisar de um segundo serviço/container.
- **Tabulator via CDN**: renderização da tabela de agendamentos no front-end, com busca/filtro.
- **Variáveis de ambiente (`.env` + `python-dotenv`)**: nenhuma credencial ou configuração sensível fica hardcoded no código.

---

# Roadmap

## Sprint 0 - Planejamento

- [x] Criar repositório
- [x] Configurar Git
- [x] Estrutura do projeto
- [x] Ambiente virtual
- [x] Dependências

## Sprint 1 - Configuração da Aplicação

- [x] Flask
- [x] Rotas (login, agenda)
- [x] Configuração

## Sprint 2 - Banco de Dados

- [x] Conexão SQLite (app/database.py)
- [x] Tabela de usuários
- [x] Estrutura de agendamentos
- [x] Seed (usuário de teste)

## Sprint 3 - Autenticação

- [x] Login
- [x] Sessão
- [x] Logout

## Sprint 4 - API

- [x] API simulada
- [x] Integração HTTP

## Sprint 5 - Agenda

- [ ] Tabulator
- [ ] Busca
- [ ] Filtros

## Sprint 6 - Tratamento de Erros

- [ ] Logs
- [ ] Exceções
- [ ] Mensagens

## Sprint 7 - Docker

- [ ] Dockerfile
- [ ] Docker Compose

## Sprint 8 - Finalização

- [ ] README
- [ ] Revisão
- [ ] Entrega
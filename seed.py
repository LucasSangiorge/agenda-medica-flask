from werkzeug.security import generate_password_hash
from app.database import get_connection


def criar_tabela_usuarios(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            senha_hash TEXT NOT NULL
        )
    """)


def inserir_usuario_teste(conn):
    email = "teste@email.com"
    senha_hash = generate_password_hash("123456")
    conn.execute("INSERT INTO usuarios (email, senha_hash) VALUES (?, ?)", (email, senha_hash))


def criar_tabela_agendamentos(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente TEXT NOT NULL,
            cpf TEXT NOT NULL,
            medico TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            data TEXT NOT NULL,
            horario TEXT NOT NULL,
            convenio TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)


def inserir_agendamentos_teste(conn):
    conn.execute(
        "INSERT INTO agendamentos (paciente, cpf, medico, especialidade, data, horario, convenio, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        ("João Silva", "111.111.111-11", "Dr. Carlos", "Cardiologia", "2026-07-25", "14:00", "Unimed", "Confirmado")
    )
    conn.execute(
        "INSERT INTO agendamentos (paciente, cpf, medico, especialidade, data, horario, convenio, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        ("Maria Souza", "222.222.222-22", "Dra. Ana", "Dermatologia", "2026-07-26", "09:30", "Bradesco Saúde", "Pendente")
    )
    conn.execute(
        "INSERT INTO agendamentos (paciente, cpf, medico, especialidade, data, horario, convenio, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        ("Pedro Lima", "333.333.333-33", "Dr. Carlos", "Cardiologia", "2026-07-27", "16:00", "Particular", "Cancelado")
    )


if __name__ == "__main__":
    conn = get_connection()
    criar_tabela_usuarios(conn)
    criar_tabela_agendamentos(conn)
    

    banco_populado = conn.execute ("SELECT COUNT(*) FROM usuarios").fetchone()[0] > 0
    if not banco_populado:
        inserir_usuario_teste(conn)
        inserir_agendamentos_teste(conn)
        conn.commit()
        print("Banco de dados criado e dados de teste inseridos com sucesso!")
        
    else:
        print("Banco de dados já possui dados, pulando inserção de dados de testes")

    conn.close()
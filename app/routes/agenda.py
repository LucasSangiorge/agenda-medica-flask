
from flask import Blueprint, render_template, redirect, url_for, session
from app.database import get_connection
from config import Config
import requests
import logging
import sqlite3

logger = logging.getLogger(__name__)

agenda_bp = Blueprint(
    "agenda",
    __name__
)


@agenda_bp.route("/agenda")
def agenda():
    if "usuario_id" not in session:
        return redirect(url_for("auth.login"))

    try:
        resposta = requests.get(Config.MOCK_API_URL, timeout=5)
        agendamentos = resposta.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"API de agendamento indisponivel:{e}")
        return render_template("agenda.html", agendamentos=[], erro="Não foi possível carregar os agendamentos no momento. Tente novamente mais tarde.")

    if not isinstance(agendamentos, list):
        logger.error("Resposta da API em formato inválido")
        return render_template("agenda.html", agendamentos=[], erro="Dados de agendamentos inválidos.")

    campos_obrigatorios = ["paciente", "cpf", "medico", "especialidade", "data", "horario", "convenio", "status"]

    for agendamento in agendamentos:
        for campo in campos_obrigatorios:
            if campo not in agendamento:
                logger.warning(f"Agendamento com campo ausente: {campo}")
                agendamento[campo] = "—"

    return render_template("agenda.html", agendamentos=agendamentos)

@agenda_bp.route("/api/agendamentos")
def api_agendamentos():
    try:
        conn = get_connection()
        linhas = conn.execute("SELECT * FROM agendamentos").fetchall()
        conn.close()
    except sqlite3.Error as e:
        logger.error(f"Erro ao acessar o banco de dados: {e}")
        return{"erro":"Erro ao acessar o banco de dados"},500
    
    agendamentos = [dict(linha) for linha in linhas]
    return agendamentos

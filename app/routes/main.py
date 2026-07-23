
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from app.database import get_connection
import requests
from config import Config

main_bp = Blueprint(
    "main",
    __name__
)


@main_bp.route("/")
def home():
    return {
        "status" : "online",
        "aplicação" : "Agenda Médica"
    }


@main_bp.route("/login", methods=["GET", "POST"])
    
def login():
    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email")
    senha = request.form.get("senha")

    conn = get_connection()
    usuario = conn.execute("SELECT * FROM usuarios WHERE email = ?", (email,)).fetchone()
    conn.close()

    if usuario is None or not check_password_hash(usuario["senha_hash"], senha):
        return render_template("login.html", erro="E-mail ou senha inválidos")

    session["usuario_id"] = usuario["id"]
    return redirect(url_for("main.agenda"))

@main_bp.route("/logout")
def logout():
    session.pop("usuario_id", None)
    return redirect(url_for("main.login"))
    

@main_bp.route("/agenda")
def agenda():
    if "usuario_id" not in session:
        return redirect(url_for("main.login"))
    
    resposta = requests.get(Config.MOCK_API_URL)
    agendamentos = resposta.json()
    return render_template("agenda.html", agendamentos=agendamentos)

@main_bp.route("/api/agendamentos")
def api_agendamentos():
    conn = get_connection()
    linhas = conn.execute("SELECT * FROM agendamentos").fetchall()
    conn.close()
    agendamentos = [dict(linha) for linha in linhas]
    return agendamentos
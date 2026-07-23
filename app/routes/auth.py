
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from app.database import get_connection
import logging

logger = logging.getLogger(__name__)

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/")
def home():
    return {
        "status" : "online",
        "aplicação" : "Agenda Médica"
    }


@auth_bp.route("/login", methods=["GET", "POST"])
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
    return redirect(url_for("agenda.agenda"))


@auth_bp.route("/logout")
def logout():
    session.pop("usuario_id", None)
    return redirect(url_for("auth.login"))

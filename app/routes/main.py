
from flask import Blueprint, render_template

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


@main_bp.route("/login")
def login():
    return render_template("login.html")

@main_bp.route("/agenda")
def agenda():
    return render_template("agenda.html")
from flask import Blueprint, render_template, request
from flask_login import LoginManager, logout_user
import flask_login
from models.user.user import User
from models.db import db
paginas = Blueprint("paginas", __name__, template_folder="./templates/", static_folder="./static/")

@paginas.route("/home")
def home():
    return render_template("home.html")

@paginas.route("/lixo")
def lixo():
    return render_template("lixo.html")

users = {"adm":"senha"}

@paginas.route("/gerenciar-usuarios", methods=["GET", "POST", "PATCH", "DELETE"])
def cadastrar_usuario():
    global users
    if request.method == "GET":
        usuarios = User.query.all()
        return render_template("gerenciar-usuarios.html", usuarios=usuarios)
    elif request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        if User.query.filter_by(username=nome).first():
            return "<h2> Nome de usuário já existe. </h2>"
        new_user = User(username=nome, password=senha)
        db.session.add(new_user)
        db.session.commit()
        return "<h2> Usuário cadastrado com sucesso </h2>"
    elif request.method == "PATCH":
        nome_antigo = request.form["nome-antigo"]
        nome_novo = request.form["nome-novo"]
        senha_nova = request.form["senha-nova"]
        user = User.query.filter_by(username=nome_antigo).first()
        if not user:
            return "<h2> Usuário não existente </h2>"
        user.username = nome_novo
        user.password = senha_nova
        db.session.commit()
        return "<h2> Usuário modificado com sucesso </h2>"
    elif request.method == "DELETE":
        nome = request.form["nome"]
        user = User.query.filter_by(username=nome).first()
        if not user:
            return "<h2> Usuário não existente </h2>"
        db.session.delete(user)
        db.session.commit()
        return "<h2> Usuário removido com sucesso </h2>"
        
@paginas.route("/")
def first():
    return "<script> window.location.href = '/login' </script>"

@paginas.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        nome = request.form["user"]
        senha = request.form["senha"]
        user = User.query.filter_by(username=nome).first()
        if user and user.password == senha:
            return "<script> window.location.href = '/lixo' </script>"
        else:
            return "<h4> Senha incorreta ou usuário inexistente </h4>"

sensores = {}
atuadores = []

@paginas.route("/gerenciar-equipamento")
def cadastrar_equipamento():
    return render_template("gerenciar-equipamento.html")

@paginas.route("/gerenciar-sensor", methods=["POST", "DELETE"])
def cadastrar_sensor():
    global sensores
    if request.method == "POST":
        sensor = request.form["sensor"]
        valor = request.form["valor"]
        if sensor in sensores:
            return "<h2> Sensor já cadastrado </h2>"
        sensores[sensor] = valor
        return "<h2> Sensor cadastrado com sucesso </h2>"
    elif request.method == "DELETE":
        sensor = request.form["sensor"]
        if sensor not in sensores:
            return "<h2> Sensor não existe </h2>"
        sensores.pop(sensor)
        return "<h2> Sensor deletado com sucesso </h2>"

@paginas.route("/gerenciar-atuador", methods=["POST", "DELETE"])
def cadastrar_atuador():
    global atuadores
    if request.method == "POST":
        atuador = request.form["atuador"]
        if atuador in atuadores:
            return "<h2> Atuador já cadastrado </h2>"
        atuadores.append(atuador)
        return "<h2> Atuador cadastrado com sucesso </h2>"
    elif request.method == "DELETE":
        atuador = request.form["atuador"]
        if atuador not in atuadores:
            return "<h2> Atuador não existe </h2>"
        atuadores.remove(atuador)
        return "<h2> Atuador removido com sucesso </h2>"

@paginas.route("/equipamento")
def sensores_f():
    global sensores
    global atuadores
    return render_template("equipamento.html", sensores=sensores, atuadores=atuadores)






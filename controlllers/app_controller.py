from flask import Flask, render_template
from models.db import db, instance
from models.iot.read import Read
from paginas import paginas
from flask_mqtt import Mqtt
from controlllers.senha_bd import senha_bd
from flask_login import LoginManager, logout_user
import flask_login

# Inicialize o gerenciador de login
login_manager = flask_login.LoginManager()

# Importe a classe de usuário
from models.user.user import User

def create_app():
    app = Flask(__name__, template_folder="./templates", static_folder="./static/")

    app.register_blueprint(paginas)

    app.config["TESTING"] = False
    app.config["SECRET_KEY"] = senha_bd
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    db.init_app(app)
    app.config["MQTT_BROKER_URL"] = "broker.hivemq.com"
    app.config["MQTT_BROKER_PORT"] = 1883
    login_manager.init_app(app)
    
    mqtt_client = Mqtt()
    mqtt_client.init_app(app)
    
    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Broker conectado")
            mqtt_client.subscribe("/eccsc-lixo-dados")
        else:
            print(f"Conexão ruim. Código: {rc}")
    
    @mqtt_client.on_disconnect()
    def handle_disconnect(client, userdata, rc):
        print("Desconectado do broker")
    
    peso = 0.0
    dist = 0.0
    resp = True
    
    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        if message.topic == "/eccsc-lixo-dados":
            mens = str(message.payload.decode("utf-8"))
            peso = float(mens.split(" ")[0])
            dist = float(mens.split(" ")[1])
            Read.save_read(1, peso, dist)
            resp = peso > 4.5 or dist < 10
            mqtt_client.publish("/eccsc-lixo-resp", resp.to_bytes())
            print(f"Peso: {peso}, dist: {dist}, resp: {resp}")
    
    @app.route("/comando")
    def comando():
        mqtt_client.publish("/eccsc-lixo-comando", True.to_bytes())
        return "<h2> Comando enviado </h2>"
    
    @app.route("/dados-tempo-real")
    def index():
        return render_template("dados-tempo-real.html", peso=peso, dist=dist, resp=resp)

    return app

# Defina a função user_loader para carregar um usuário com base no ID do usuário
@login_manager.user_loader
def load_user(user_id):
    return User.get_user(user_id)

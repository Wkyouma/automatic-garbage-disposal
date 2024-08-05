from controlllers.app_controller import create_app
from utils.create_db import create_db

if __name__ == "__main__":
    app = create_app()
    create_db(app)
    app.run(host="0.0.0.0", port=8080, debug=True)



# Parte do Flask e comunicação com o usuário
# app.register_blueprint(paginas)

# Parte do MQTT
# app.config["MQTT_BROKER_URL"] = "broker.hivemq.com"
# app.config["MQTT_BROKER_PORT"] = 1883

# mqtt_client = Mqtt()
# mqtt_client.init_app(app)

# @mqtt_client.on_connect()
# def handle_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print("Broker conectado")
#         mqtt_client.subscribe("/eccsc-lixo-dados")
#     else:
#         print(f"Conexão ruim. Código: {rc}")

# @mqtt_client.on_disconnect()
# def handle_disconnect(client, userdata, rc):
#     print("Desconectado do broker")

# peso = 0.0
# dist = 0.0
# resp = True

# @mqtt_client.on_message()
# def handle_mqtt_message(client, userdata, message):
#     if message.topic == "/eccsc-lixo-dados":
#         global peso
#         global dist
#         global resp
#         mens = str(message.payload.decode("utf-8"))
#         peso = float(mens.split(" ")[0])
#         dist = float(mens.split(" ")[1])
#         resp = peso > 4.5 or dist < 10
#         global mqtt_client
#         mqtt_client.publish("/eccsc-lixo-resp", resp.to_bytes())
#         print(f"Peso: {peso}, dist: {dist}, resp: {resp}")

# @app.route("/comando")
# def comando():
#     mqtt_client.publish("/eccsc-lixo-comando", True.to_bytes())
#     return "<h2> Comando enviado </h2>"

# @app.route("/dados-tempo-real")
# def index():
#     global peso
#     global dist
#     global resp
#     return render_template("dados-tempo-real.html", peso=peso, dist=dist, resp=resp)

# print("comecou app")
# app.run(port=80, debug=False)

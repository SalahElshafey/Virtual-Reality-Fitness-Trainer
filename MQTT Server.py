import paho.mqtt.client as mqtt
import ssl

broker = "971539a03b5648de94b5aa970021d2f0.s1.eu.hivemq.cloud"
port = 8883
username = "SalahElshafey"
password = "Salah2025"

client = mqtt.Client()
client.username_pw_set(username, password)
client.tls_set(tls_version=ssl.PROTOCOL_TLS)

client.connect(broker, port)
client.publish("vrfitness/classname", "Pushup")
client.disconnect()

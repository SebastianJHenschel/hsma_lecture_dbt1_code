import paho.mqtt.client as mqtt

_username = "your_username"
_passwd = "your_password"
_host = "your_host"
_port = 1883 
_timeout = 60 

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("dbt1/#")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload.decode("utf-8"))) 

client = mqtt.Client()
client.username_pw_set(_username, _passwd)
client.on_connect = on_connect
client.on_message = on_message

client.connect(_host, _port, _timeout)

client.loop_forever()
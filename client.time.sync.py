import paho.mqtt.client as mqtt
import datetime

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")
    client.subscribe("$time")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    # datetime ref: http://www.wklken.me/posts/2015/03/03/python-base-datetime.html#1-datetime_1
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": "+str(msg.payload))

client = mqtt.Client(client_id="paho.client.time.sync")
client.on_connect = on_connect
client.on_message = on_message

client.connect("121.40.130.184", 1883, 60)
# client.connect("127.0.0.1", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

import paho.mqtt.client as mqtt

def on_publish(mosq, userdata, mid):
    mosq.disconnect()

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)
client.on_publish = on_publish

f=open("/home/logan/Pictures/iot.png", "rb") #3.7kiB in same folder
fileContent = f.read()
byteArr = bytearray(fileContent)
client.publish("image",byteArr,0)

client.loop_forever()

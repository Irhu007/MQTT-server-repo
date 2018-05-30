import paho.mqtt.client as mqtt

def on_connect(self,client, userdata, rc):
    print("Connect" + str(rc))
    self.subscribe("image") 

def on_message(client, userdata, msg):
    print "Topic : ", msg.topic
    f = open("/home/logan/Downloads/object-detection-deep-learning/images/output.png", "w")
    f.write(msg.payload)
    f.close()

client = mqtt.Client()
client.connect("192.168.43.122",1883,60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

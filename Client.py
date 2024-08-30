import paho.mqtt.client as mqtt
import serial

# Define the callback function that is called when the client successfully connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
	print("Connected to MQTT")
	print("Connection returned result: " + str(rc) )
	client.subscribe("home/livingroom/light")

# Define the callback function that is called when a message is received on a subscribed topic
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	ser = serial.Serial("/dev/rfcomm0", 9600)	                        ser.write(msg.payload) 

client = mqtt.Client() # Create a new instance of the MQTT client
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
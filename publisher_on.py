import paho.mqtt.publish as publish  

# Publish a single message to the specified MQTT topic
publish.single("home/livingroom/light", "LED_ON",hostname="test.mosquitto.org")  
print("Done")  

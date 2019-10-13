import time
from umqttsimple import MQTTClient
import ubinascii
import machine

# MQTT Configs 
mqtt_server = 'www.maqiatto.com'
client_id = ubinascii.hexlify(machine.unique_id())

def connect(mqtt_user = "jef.oli@gmail.com", mqtt_pass = "jef@#123"):
  global client
  client = MQTTClient(client_id, mqtt_server, 1883, mqtt_user, mqtt_pass)
  client.connect()
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client
  
def subscribe(topic, callback):
  client.set_callback(callback)
  client.subscribe(topic)
  print('Subscribed to %s topic' % (topic))
  
def check_msg():
  client.check_msg()

def publish(topic, message):
  client.publish(topic, str(message))



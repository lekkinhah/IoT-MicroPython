
import time
from umqttsimple import MQTTClient
import ubinascii
import machine

# MQTT Configs 
mqtt_server = 'mqtt.thingspeak.com'
client_id = ubinascii.hexlify(machine.unique_id())
write_api_key = 'N0B2HN0ECFIN0UGP'

def connect(mqtt_user = "jef.oli@gmail.com", mqtt_pass = "jef@#123"):
  global client
  client = MQTTClient(client_id, mqtt_server, 1883)
  client.connect()
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client
  
def subscribe(topic, callback):
  client.set_callback(callback)
  client.subscribe(topic)
  print('Subscribed to %s topic' % (topic))
  
def check_msg():
  client.check_msg()

def publish_temp(value):
  topic= 'channels/878804/publish/' + write_api_key
  payload = 'field1='+str(value)
  client.publish(topic, payload)
 
def publish_hum(value):
  topic= 'channels/878804/publish/' + write_api_key
  payload = 'field2='+str(value)
  client.publish(topic, payload)




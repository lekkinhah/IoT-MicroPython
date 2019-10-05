import time
from umqttsimple import MQTTClient
import ubinascii
import machine

# MQTT Configs 
mqtt_server = 'www.maqiatto.com'
client_id = ubinascii.hexlify(machine.unique_id())

def sub_cb(topic, msg):
  if msg is not None:        
    print("MESSAGE:")
    print(msg)

def connect(mqtt_user = "jef.oli@gmail.com", mqtt_pass = "jef@#123"):
  global client = MQTTClient(client_id, mqtt_server, 1883, mqtt_user, mqtt_pass)
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

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()
  
def start_subscription(message_interval = 5):
  try:
    client = connect()
    subscribe(client, b'jef.oli@gmail.com/test', sub_cb)
    last_message = 0

    while True:
      try:
        client.check_msg()
        if (time.time() - last_message) > message_interval:
          client.publish(topic_pub, "TESTE")
          last_message = time.time()
      except OSError as e:
        restart_and_reconnect()
    
  except OSError as e:
    restart_and_reconnect()


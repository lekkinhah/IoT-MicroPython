

# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

import uos, machine

#uos.dupterm(None, 1) # disable REPL on UART(0)

import gc

#import webrepl

#webrepl.start()

#import _thread
import time
import wifi
import maqiatto
import light
import humidity

gc.collect()

def light_listener(topic, message):
  if message == b'on':
    light.turn_on()
  else:
    light.turn_off()
    
  print('Lights %s !!' % (message))

#_thread.start_new_thread(wifi.connect, ("MyASUS", "senha555"))
wifi.connect("MyASUS", "senha555")
maqiatto.connect()
maqiatto.subscribe("jef.oli@gmail.com/light", light_listener)

while True:
  maqiatto.check_msg()
  humidity_val = humidity.read()
  print(humidity_val)
  maqiatto.publish("jef.oli@gmail.com/humidity", humidity_val)
  time.sleep(3)


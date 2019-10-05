from machine import Pin
import time
import dht

ledred = Pin(5, Pin.OUT)
ledblue = Pin(4, Pin.OUT)
ledyellow = Pin(16, Pin.OUT)
dht = dht.DHT11(Pin(2))

def read_output(value):  
  if value > 76:
    ledred(1)
    ledblue(0)
  else:
    ledred(0)
    ledblue(1)
    
def read_outputTemp(valueT):
  if valueT > 22:
    ledyellow(0)
    time.sleep(0.05)
    ledyellow(1)
  else:
    ledyellow(0)

def read():
  dht.measure()
  value_hum = dht.humidity()
  value_temp = dht.temperature()
  read_output(value_hum)
  read_outputTemp(value_temp)
  return value_hum, value_temp




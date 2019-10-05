import network
from machine import Pin
import time

sta_if = network.WLAN(network.STA_IF)
led = Pin(0, Pin.OUT)

def connecting_output():
  led(1)
  time.sleep(0.05)
  led(0)
  time.sleep(0.05)
  
def connected_output():
  connecting_output()
  led(1)
  print("connected!!!")
  print(sta_if.ifconfig())

def connect(ssid = "IOT", password = "12345678"):
  sta_if.active(True)
  
  if sta_if.isconnected():
    connected_output()

  while True:
    if not sta_if.isconnected():
      print("connecting to " + ssid)
      sta_if.connect(ssid, password)      
      
      while not sta_if.isconnected():        
        connecting_output()
        pass
      
      connected_output()
  

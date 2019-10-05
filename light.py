from machine import Pin

led = Pin(16, Pin.OUT)

def turn_on():
  led(1)

def turn_off():
  led(0)  


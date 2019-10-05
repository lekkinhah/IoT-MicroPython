from machine import Pin
import time

ledgreen = Pin(16, Pin.OUT)
ledred = Pin(5, Pin.OUT)
ledblue = Pin(4, Pin.OUT)
ledyellow = Pin(0, Pin.OUT)

for i in range(10):
  ledgreen(1)
  time.sleep(0.05)
  ledred(1)
  time.sleep(0.05)
  ledblue(1)
  time.sleep(0.05)
  ledyellow(1)
  time.sleep(0.05)
  ledgreen(0)
  time.sleep(0.05)
  ledred(0)
  time.sleep(0.05)
  ledblue(0)
  time.sleep(0.05)
  ledyellow(0)
  time.sleep(0.05)
  






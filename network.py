import network

def connect(ssid = "IOT", password = "12345678"):
  sta = network.WLAN(network.STA_IF)
  sta.active(True)
  sta.connect(ssid, password)
  print(sta.isconnected())
  print(sta.ifconfig())
  print(sta.status())


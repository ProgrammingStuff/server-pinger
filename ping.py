import os
import time

def ping(address):
  os.system("ping -c 1 address")
   
while True:
  ping("uhc-server.herokuapp.com")
  time.sleep(600)

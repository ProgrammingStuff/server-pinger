import os
import time

def ping(address):
  os.system("ping -c 1 address")
   
while True:
  ping("google.com")
  time.sleep(600)

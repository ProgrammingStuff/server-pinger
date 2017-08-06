import os
import time

def ping(address):
  return not os.system('ping %s -n 1' % (address,))
   
while True:
  ping("uhc-server.herokuapp.com")
  time.sleep(600)

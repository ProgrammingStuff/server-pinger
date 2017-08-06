import os
import time
  def ping(address):
    return not os.system('ping %s -n 1' % (address,))
   
   while True:
   ping("httpss://uhc-server.herokuapp.com")

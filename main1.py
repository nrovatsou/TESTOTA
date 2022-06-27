from ota_updater import OTAUpdater
import wifimgr
import utime, ubinascii, math   #add urequests fro google sheets
from machine import I2C, ADC, Pin

from time import sleep
#import machine





def download_and_install_update_if_available():
     o = OTAUpdater('url-to-your-github-project')
     o.install_update_if_available_after_boot('wifi-ssid', 'wifi-password')

def deepsleep (duration):
    for y in range(0,10):
      try:
        import machine
        #print('Going to Deep Sleep now...')
        machine.deepsleep(duration) #milliseconds
      except:
        utime.sleep_ms(500) 

def start():
     # your custom code goes here. Something like this: ...
     # from main.x import YourProject
     # project = YourProject()
     # ...
     from ntptime import settime
     
     while(1):
      try:
       settime()
       print("Time Set")
       utime.sleep_ms(2000)
      except:
       print("No Internet, Time not Set")
       deepsleep(30000)	

       idx=idx+1
       print("Occurence: ", idx, " Counter: ", counter)

def boot():
     download_and_install_update_if_available()
     start()

def connectwifi():
     wlan = wifimgr.get_connection()
     if wlan is None:
          print("Could not initialize the network connection.")
          deepsleep(60000)

boot()
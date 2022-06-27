#import machine
import utime
import wifimgr
from ntptime import settime

def x():
 print("This is x")

def maint():
 print("Hello it works")


def deep (duration):
    for y in range(0,10):
      try:
        import machine
        #print('Going to Deep Sleep now...')
        machine.deepsleep(duration) #milliseconds
      except:
        utime.sleep_ms(500) 

def Internetime():
     try:
        settime()
        print("Time Set")
        utime.sleep_ms(2000)
     except:
        print("No Internet, Time not Set")
        deep(30000)

def connectwifi():
     wlan = wifimgr.get_connection()
     if wlan is None:
          print("Could not initialize the network connection.")
          deep(60000)




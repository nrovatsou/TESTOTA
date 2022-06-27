import wifimgr
from time import sleep
import machine
import utime, ubinascii, math   #add urequests fro google sheets
from machine import I2C, ADC, Pin
from ntptime import settime
from umqttsimple import MQTTClient
#import BlynkLib_mp
import os
import array
# import urequests as requests    #Uncomment for google sheets
import gc  
from machine import WDT
import socket, ussl

from ota_updater import OTAUpdater



def deepsleep (duration):
    for y in range(0,10):
      try:
        import machine
        #print('Going to Deep Sleep now...')
        machine.deepsleep(duration) #milliseconds
      except:
        utime.sleep_ms(500) 

wlan = wifimgr.get_connection()
print("WLAN is: ", wlan)
if wlan is None:
    print("Could not initialize the network connection.")
    deepsleep(60000)
idx=0 
mqtt_server = '79.131.103.193'
#client_id = ubinascii.hexlify(machine.unique_id())
client_id='maria_client_1'


#client_id = machine.unique_id()
#cl="Maria" 
print("ClientID: ", client_id)   
last_message = 0
message_interval = 15
counter = 0
topic_pub=b'master/maria_client_1/writeattributevalue/Number/4H2V9mRKEM6ucicPPE9B13'

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  utime.sleep_ms(10000)
  machine.reset()

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server, port=8883, user="master:mqttuser", password="Ia5q732s4jOKusvpOH0OPywR2vcSOQbd", ssl=True)  
  #def __init__(self, client_id, server, port=0, user=None, password=None, keepalive=0, ssl=False, ssl_params={}):
  #client.set_callback(sub_cb)
  print("Opening connection.....")
  client.connect()
  #client.subscribe(topic_sub)
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

try:
  
  client = connect_and_subscribe()
except OSError as e:
  #error = os.strerror(e)
  print("Error: ", e)
  utime.sleep_ms(10000)
  restart_and_reconnect()  

while(1):
 try:
  settime()
  print("Time Set")
 except:
  print("No Internet, Time not Set")
  deepsleep(30000)	

 

 idx=idx+1
 print("Occurence: ", idx, " Counter: ", counter)

 try:
  #msg = b'Hello #%d' % counter
  msg1=counter*12
  msg=str(msg1)
  client.publish(topic_pub, msg)
  counter += 1
  print ("Message SENT!")
 except OSError as e:
    print("Error Sending Message: ", e)
    utime.sleep_ms(10000)
    restart_and_reconnect()

 utime.sleep_ms(20000)
 
 print("Relooping......")


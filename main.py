import os
import sys
sys.path.append("app")
from ota_updater import OTAUpdater
import utime, ubinascii, math   #add urequests fro google sheets
from machine import I2C, ADC, Pin

from time import sleep
import tasos


def download_and_install_update_if_available():
     
     tasos.connectwifi()
     o = OTAUpdater('https://github.com/nrovatsou/TESTOTA')
     print("-------------------------------")
     print("GitHub Repo", o.github_repo)
     print("Main dir: ", o.main_dir)
     print("New version dir: ", o.new_version_dir)
     print("----------------------------------------")
     o.check_for_update_to_install_during_next_reboot()
     o.install_update_if_available_after_boot('COSMOTE-179663', 'DYR7K3QY7HDU469A')

def start():
     # your custom code goes here. Something like this: ...
     # from main.x import YourProject
     # project = YourProject()
     # ...
    import tasos 

    print("Starting R2....")
    
    tasos.Internetime()
    tasos.x()
    utime.sleep_ms(2000)
    tasos.maint()
    tasos.deep(10000)


def boot():
     download_and_install_update_if_available()
     start()


boot()     






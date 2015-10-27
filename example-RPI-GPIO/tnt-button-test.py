#!/usr/bin/env python

import RPi.GPIO as GPIO # 
from time import sleep # damit du Pausen einbauen kannst in deinen Code

GPIO.setmode(GPIO.BCM) #du kannst zwischen zwei Pin Nummerierungsmodes wählen

GPIO.setup(24, GPIO.IN) #setzt GPIO24 als Input


try: 
    while True:  
        if GPIO.input(24):  
            print('Button Gedrückt') 
        else: 
        sleep(0.2)  # warte 0.1 Sekunde
except KeyboardInterrupt:
        GPIO.cleanup()  #resete den Pin 24 wieder




#!/usr/bin/env python

#verbinde ein Jumperkabel mit GPIO24 und das ander mit GND
#im Terminal tippe sudo geany ein, bei Kano ist geany schon vorinstalliert, solltest du 
#raspian nutzen musst du geany erst mit sudo apt-get install geany installieren

import RPi.GPIO as GPIO # import RPi.GPIO Modul
from time import sleep # damit du Pausen einbauen kannst in deinen Code

GPIO.setmode(GPIO.BCM) #du kannst zwischen zwei Pin Nummerierungsmodes wählen

GPIO.setup(24, GPIO.IN) #setzt GPIO24 als Input


try: 
    while True:  
        if GPIO.input(24):  
            print "Button gedrückt" 
        else: 
            print "Button nicht gedrückt"
        sleep(0.1)  # warte 0.1 Sekunde
except KeyboardInterrupt:
        GPIO.cleanup()  #resete den Pin 24 wieder




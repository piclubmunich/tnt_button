#!/usr/bin/env python

import RPi.GPIO as GPIO # 
from time import sleep # damit du Pausen einbauen kannst in deinen Code

GPIO.setmode(GPIO.BCM) #du kannst zwischen zwei Pin Nummerierungsmodes wählen, hier wählen wir BCM

GPIO.setup(24, GPIO.IN) #setzt GPIO24 als Input


try: 
    while True:  # das ist eine Endlosschleife, die mit CTRL+C stoppen kannst   
        if GPIO.input(24):  #when GPIO24 == 1 als wenn der Button gedrückt wird
            print('Button Gedrückt')  #schreibe Button Grdückt
        else: 
            print("Drücke Button") #wenn Button nicht gedrückt dann schreibe Drücke Button
        sleep(0.2)  # warte 0.1 Sekunde
except KeyboardInterrupt:
        GPIO.cleanup()  #resete den Pin 24 wieder




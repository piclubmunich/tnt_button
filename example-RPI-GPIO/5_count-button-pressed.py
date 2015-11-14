#!/usr/bin/env python

#zaehle wievil mal du auf den button drueckst

import RPi.GPIO as GPIO # importiere das RPi.GPIO Modul
from time import sleep # damit du Pausen einbauen kannst in deinen Code

GPIO.setmode(GPIO.BCM) #du kannst zwischen zwei Pin Nummerierungsmodes wählen, hier waehlen wir BCM

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setzt GPIO24 als Input mit pull-up
count = 0

try: 
    while True:  # das ist eine Endlosschleife, die mit CTRL+C stoppen kannst   
        mein_button = GPIO.input(24) #setze GPIO24 gleich der Variable mein_button
        if mein_button == False:  #wenn Button nicht nicht gedrueckt wird
          count = count+1
          print " count", count
          sleep(0.1)

finally:
        GPIO.cleanup()  #resete den GPIO24 wieder

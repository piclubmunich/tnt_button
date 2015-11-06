#!/usr/bin/env python

#zu halloween lade dir einen schoenen Schreisound herunter es sollte ein mp3 sein
# mit Internet Verbindung tippe folgendens sudo apt-get install mpg123
#du kannst es den song so abspielen mpg123 MySong.mp3

import RPi.GPIO as GPIO # importiere das RPi.GPIO Modul
import os
from time import sleep # damit du Pausen einbauen kannst in deinen Code

GPIO.setmode(GPIO.BCM) #du kannst zwischen zwei Pin Nummerierungsmodes wählen, hier waehlen wir BCM

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setzt GPIO24 als Input mit pull-up


try: 
    while True:  # das ist eine Endlosschleife, die mit CTRL+C stoppen kannst   
        button_state = GPIO.input(24) #setze GPIO24 gleich der Variable button_state
        if button_sate == False:  #wenn Button nicht nicht gedrueckt wird
            os.system('mpg123 minecraft_short.mp3 &') #play sound with the name minecraft_short.mp3
            #print "Button gedrueckt"  #schreibe Button gedrueckt
        else: 
            print "Press Button to Play Sound" 
        sleep(0.1)

finally:
        GPIO.cleanup()  #resete den GPIO24 wieder

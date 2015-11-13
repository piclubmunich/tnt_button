#schreibe den Code geradde

#!/usr/bin/env python
#checke ob der omxplayer installiert ist omxplayer --version
#install wenn noch nicht installiert sudo apt-get install omxplayer
#erstelle einen ordner videos


import RPi.GPIO as GPIO # importiere das RPi.GPIO Modul
import os
from time import sleep # damit du Pausen einbauen kannst in deinen Code

GPIO.setmode(GPIO.BCM) #du kannst zwischen zwei Pin Nummerierungsmodes waehlen, hier waehlen wir BCM

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setzt GPIO24 als Input mit pull-up


try: 
    while True:  # das ist eine Endlosschleife, die mit CTRL+C stoppen kannst   
        button_state = GPIO.input(24) #setze GPIO24 gleich der Variable button_state
        if button_state == False:  #wenn Button nicht nicht gedrueckt wird
            os.system("omxplayer -o hdmi /home/user/videos/ [Media File].m4v")
            #print "Button gedrueckt"  #schreibe Button gedrueckt
        else: 
            print "Press Button to Play Sound" 
        sleep(0.1)

finally:
        GPIO.cleanup()  #resete den GPIO24 wieder

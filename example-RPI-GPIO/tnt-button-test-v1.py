#!/usr/bin/env python

#jetzt verbessern wir den Code indem wir pull-ups verwenden
#wenn man keine pull-up oder pull-down Widerstaende verwendet ist der Status des Inputs nicht klar definiert er floatet
#der Input kann sich deshalb aendern lediglich, durch die Statische Ladung von dir und der Button koennte willkuerlich ausgeloest werden
#wenn wir keine Widerstaende verwenden wollen, koennen wir Software im Raspberry Pi verwenden, um dem Input einen
#klaren Status zu geben

import RPi.GPIO as GPIO # importiere das RPi.GPIO Modul
from time import sleep # damit du Pausen einbauen kannst in deinen Code

GPIO.setmode(GPIO.BCM) #du kannst zwischen zwei Pin Nummerierungsmodes wählen, hier waehlen wir BCM

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #setzt GPIO24 als Input mit pull-up


try: 
    while True:  # das ist eine Endlosschleife, die mit CTRL+C stoppen kannst   
        if GPIO.input(24):  #when GPIO24 == 1 als wenn der Button gedrückt wird
            print('Button nicht gedrückt')  #schreibe Button Grdückt, dass ist nun genau anders herum will wir einen pull-up gesetzt haben
        else: 
            print("Button gedrueckt") #wenn Button nicht gedrückt dann schreibe Drücke Button
        sleep(0.1)  # warte 0.1 Sekunde

finally:
        GPIO.cleanup()  #resete den Pin 24 wieder


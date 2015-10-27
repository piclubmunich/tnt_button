#!/usr/bin/env python

#jetzt verbessern wir den Code indem wir pull-ups verwenden
#wenn man keine pull-up oder pull-down Widerstände verwendet ist der Status des Input Pins nicht klar definiert er floatet
#der Input kann sich deshalb ändern lediglich, durch die Statische Ladung von dir 
#wenn wir keine Widerstände vewenden wollen, können wir Software im Raspberry Pi verwenden, um dem Input einen
#klaren Status zu geben

import RPi.GPIO as GPIO # importiere das RPi.GPIO Modul
from time import sleep # damit du Pausen einbauen kannst in deinen Code

GPIO.setmode(GPIO.BCM) #du kannst zwischen zwei Pin Nummerierungsmodes wählen, hier wählen wir BCM

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #setzt GPIO24 als Input


try: 
    while True:  # das ist eine Endlosschleife, die mit CTRL+C stoppen kannst   
        if GPIO.input(24):  #when GPIO24 == 1 als wenn der Button gedrückt wird
            print('Button Gedrückt')  #schreibe Button Grdückt
        else: 
            print("Drücke Button") #wenn Button nicht gedrückt dann schreibe Drücke Button
        sleep(0.2)  # warte 0.1 Sekunde

finally:
        GPIO.cleanup()  #resete den Pin 24 wieder

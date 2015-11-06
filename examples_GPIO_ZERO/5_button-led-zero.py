
#!/usr/bin/env python

#jetzt fügen wir eine LED hinzu

from gpiozero import LED
from gpiozero import Button
from time import sleep

GPIO.setmode(GPIO.BCM) #du kannst zwischen zwei Pin Nummerierungsmodes wählen, hier waehlen wir BCM

while True:  # das ist eine Endlosschleife, die mit CTRL+C stoppen kannst   
    if button.is_active:  #wenn Button nicht nicht gedrueckt wird 
        print "Button gedrueckt"  #schreibe Button gedrueckt
        led.toggle()
    else: 
        print "Button nicht gedrueckt" #wenn Button nicht gedrueckt, wenn du willst kannst due jetzt auch das ganze Else wegloeschen
        sleep(0.1)


#!/usr/bin/env python

#jetzt verbinde eine LED mit deinem Pi, ein Jumper zu GPIO17 und einer zu GND

from gpiozero import LED
from gpiozero import Button
from time import sleep

button = Button(24)
led = LED(17)

while True:  # das ist eine Endlosschleife, die mit CTRL+C stoppen kannst   
    if button.is_active:  #wenn Button nicht nicht gedrueckt wird 
        print "Button gedrueckt"  #schreibe Button gedrueckt
        led.toggle()
    else: 
        print "Button nicht gedrueckt" #wenn Button nicht gedrueckt, wenn du willst kannst due jetzt auch das ganze Else wegloeschen
        sleep(0.1)

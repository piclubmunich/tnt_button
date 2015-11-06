#!/usr/bin/env python
from gpiozero import Button
from time import sleep

button = Button(24)

# Button(pin=24, pull_up=True, bounce_time=None)


while True:
    if button.is_active:
        print "Button Pressed"
       
        sleep(0.5)
    else:
        print "press Button"

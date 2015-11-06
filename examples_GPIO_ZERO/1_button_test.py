#!/usr/bin/env python
from gpiozero import Button
from time import sleep


button = Button(24)


while True:
    if button.is_active:
        print "Button Pressed"
       
        sleep(0.5)
    else:
        print "press Button"

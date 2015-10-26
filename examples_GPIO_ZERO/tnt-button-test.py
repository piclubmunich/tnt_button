#!/usr/bin/env python
from gpiozero import LED
from gpiozero import Button
from time import sleep


button = Button(24)


while True:
    if button.is_active:
        print('Button Pressed')
       
        sleep(0.5)
    else: tnt
        print('press button to launch tnt')

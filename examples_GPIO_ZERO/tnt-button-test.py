#!/usr/bin/env python
from gpiozero import LED
from gpiozero import Button
from time import sleep


import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block


button = Button(24)


while True:
    if button.is_active:
        print('Button Pressed')
       
        sleep(0.5)
    else: tnt
        print('press button to launch tnt')

#!/usr/bin/env python

#jetzt verbinden wir den Button mit Minecraft eine Anleitung dazu findet du im Readme

import RPi.GPIO as GPIO  # importiere das RPi.GPIO Modul
from time import sleep   # damit du Pausen einbauen kannst in deinen Code

import mcpi.minecraft as minecraft  # Minecraft Module
mc = minecraft.Minecraft.create()  # Minecraft Verbindung
import mcpi.block as block  # importiere Block Modul


GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    while True:
        button_state = GPIO.input(24) #setze Input 24 gleich der Variable button_state
        if button_state == False:
            print('Button Pressed')
            mc.postToChat("TNT") #schreibe TNT in den Chat
            pos = mc.player.getPos()
            x = pos.x
            y = pos.y
            z = pos.z

            block = 46 # setze den Block gleich der ID 46, 46 ist TNT, 10 ist Wasser z.B.

           	mc.setBlock(x, y, z, block,1) #baue den Block, 0 ist nicht aktives TNT 1 ist aktives
            time.sleep(0.2)
finally:
    GPIO.cleanup() #resete den Pin 24 wieder



#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import o

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block


GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)



while True:
    input_state = GPIO.input(24)
    if input_state == False:
        print('Button Pressed')
        pos = mc.player.getPos()
        os.system('mpg123 minecraft_short.mp3 &')
        x = pos.x
        y = pos.y
        z = pos.z

        block = 46

        mc.setBlock(x, y, z, block,1)
        time.sleep(0.2)



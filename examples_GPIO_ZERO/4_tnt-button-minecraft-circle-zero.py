#!/usr/bin/env python

from gpiozero import Button
from time import sleep

import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff
mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
import mcpi.block as block

radius = 10 #bestimme den Radius deines TNT-Kreises

while True:
    if button.is_active:
        print "Button Pressed"
        mc.postToChat("TNT")
        pos = mc.player.getPos()
        x = pos.x
        y = pos.y
        z = pos.z
        block = 46
        mc.setBlock(x, y, z, block,1)	
        mcdrawing.drawCircle(x, y, z, radius, block, 1)
        sleep(0.2)
#mehr Aufgaben folgen



import RPi.GPIO as GPIO                                    # 
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)



while True:
    input_state = GPIO.input(24)
    if input_state == False:
        print('Button Pressed')
        pos = mc.player.getPos()
        x = pos.x
        y = pos.y
        z = pos.z

        block = 46

       	   mc.setBlock(x, y, z, block,1)
        time.sleep(0.2)



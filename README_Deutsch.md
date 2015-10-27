#TNT Button

Mit dem TNT Button kannst aktives TNT in Minecraft Raspberry Pi Edition setzen oder ins sonst  


#Shematic


#Examples mit RPI



#Examples with GPIO ZERO

``` 
# RPi.GPIO                        GPIO Zero
from RPi import GPIO              from gpiozero import LED
from time import sleep            from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)          led = LED(25)
GPIO.output(25,1)                 led.on()
sleep(5)                          sleep(5)
GPIO.output(25,0)                 led.off()
     ```



#TNT Button

Mit dem TNT Button kannst aktives TNT in Minecraft Raspberry Pi Edition setzen oder eine andere Aktion in Minecraft ausführen.

Du kannst den Button bei meinen Raspberry Pi Kursen erwerben. 

#Shematic

Dein Button hat zwei Pins. Nehme die beiliegenden Female to Female Steckbrücken und schließe einen GND GPIO und eine an den GPIO24 Pin des Raspberry Pis an. Nutze dein GPIO Leave damit du nicht die falschen Pins verbindest. 

Fritzing Sheamtic einfügen



#Beispiele mit RPI.GPIO

Hier habe ich ein paar Beispiel Programme für dich geschrieben.

1.
2.
3.
4.
5.
6.
7. 


#Beispiele mit GPIO ZERO

GPIO Zero ist eine neue Library die das steuern der GPIO Pins Steuern.

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

Du kannst sie installieren folgendermaßen installieren. 

http://pythonhosted.org/gpiozero/#install



#Minecraft API in Kano

#Minecraft API in Rasparian

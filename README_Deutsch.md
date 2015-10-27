#TNT Button

Mit dem TNT Button kannst aktives TNT in Minecraft Raspberry Pi Edition setzen oder eine andere Aktion in Minecraft ausführen.

Du kannst den Button bei meinen Raspberry Pi Kursen erwerben. 

#Shematic

Dein Button hat zwei Pins. Nehme die beiliegenden Female to Female Steckbrücken und schließe eine an einen GND Pin und eine an den GPIO Pin des Raspberry Pis an. 



#Beispiele mit RPI.GPIO

Hier habe ich ein paar Beispiel Programme für dich geschrieben


#Beispiele mit GPIO ZERO

GPIO Zero ist eine einfachere Library mit der man die GPIO Pins Steuern.

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

```

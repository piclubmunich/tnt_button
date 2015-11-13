#arbeite gerade am code
#bei Kano musst du erst noch pi camera installieren
#sudo easy_install --user picamera
#aktiviere die camera, tipp sudo kano-camera 
#reboote deinen pi
#tippe in das terminal ein raspistill -o image1.jpg  damit testest du ob die Kamera funktioniert 

import picamera
from RPi import GPIO

button = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

with picamera.PiCamera() as camera:
	camera.start_preview()
	frame = 1
	while True:
		GPIO.wait_for_edge(button, GPIO.FALLING)
		camera.capture('/frame%03d.jpg' % frame)
		frame += 1
		camera.stop_preview()

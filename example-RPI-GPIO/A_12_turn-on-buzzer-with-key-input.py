#arbeite an code
#sudo apt-get install  python-pip
#sudo pip install python-uinput
#sudo modprobe uinput

from time import sleep
import uinput
device =  uinput.Device((uinput.KEY_W,uinput.KEY_S))



while 1:
        device.emit(uinput.KEY_W,1)
        print "hallo"
        sleep(0.5)
        device.emit(uinput.KEY_W,0)
        print "hallo"
        time.sleep(0.5)

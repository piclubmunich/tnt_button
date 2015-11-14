#!/usr/bin/python
import RPi.GPIO as GPIO

from time import sleep
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False) #damit keine Fehlernachrichten kommen

while True:
  if not GPIO.input(11):
    flash = random.randint(1,6)
    while not GPIO.input(24):
      GPIO.output(17, True)
    while flash > 0:
      GPIO.output(17, False)
      sleep(.5)
      GPIO.output(17, True)
      sleep(.5)
      flash ­= 1
  else:
    GPIO.output(17,True)

import RPi.GPIO as GPIO
import time
import drive,motor_init
GPIO.setmode(GPIO.BCM)
motor_init.initialize()
drive.forward()
time.sleep(2)
drive.backward()

import requests
from time import sleep
import RPi.GPIO as GPIO
motor=21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(motor,GPIO.OUT)
while True:
    sleep(5)
    a=int(requests.get(url="http://data.olala.me/data/a.txt").json())
    GPIO.output(motor,a)
    
    


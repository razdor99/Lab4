#!/usr/bin/python3

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

import RPi.GPIO as GPIO
import time

ledPin1 = 19
ledPin2 = 20
ledPin3 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)

pwm1 = GPIO.PWM(ledPin1, 100) # PWM object on our pin at 100 Hz
pwm1.start(0) # start with LED off
pwm2 = GPIO.PWM(ledPin2, 100) # PWM object on our pin at 100 Hz
pwm2.start(0) # start with LED off
pwm3 = GPIO.PWM(ledPin3, 100) # PWM object on our pin at 100 Hz
pwm3.start(0) # start with LED off

import json
with open('led-pwm-multiple.txt', 'r') as f:
 data = json.load(f)
print("slider 1 = " + str(data['slider1']))


while True:
  pwm1.ChangeDutyCycle(data)
  pwm2.ChangeDutyCycle(data)
  pwm3.ChangeDutyCycle(data)
  time.sleep(0.1)
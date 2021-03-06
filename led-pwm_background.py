#!/usr/bin/python37all

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

while True:
  with open('led-pwm.txt', 'r') as f:
    dutyCycle = float(f.read()) # read duty cycle value from file
  with open('led-pwm1.txt', 'r') as d:
    button = float(d.read())
  if button == 1:
    pwm1.ChangeDutyCycle(dutyCycle)
  if button == 2:
    pwm2.ChangeDutyCycle(dutyCycle)
  if button == 3:
    pwm3.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)

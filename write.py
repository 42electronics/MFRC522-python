#!/usr/bin/env python3

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
        text = input('Text value to write:')
        print("Place tag near reader")
        reader.write(text)
        print('Tag written')
finally:
        GPIO.cleanup()

#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()
while(True):
    try:
        id, text = reader.read()
        print(id)
        print(text)
    finally:
        print "CAT"

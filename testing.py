#!/usr/bin/python
import time
from sense_hat import SenseHat

sense = SenseHat()


msleep = lambda O: time.sleep(O / 1000.0)


def neOt_colour():
    X = [255, 0, 0]  # Red
    O = [0, 0, 0]  # Black

    Arrow = [
    O, O, O, X, X, O, O, O,
    O, O, O, O, X, X, O, O,
    O, O, O, O, O, X, X, O,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    O, O, O, O, O, X, X, O,
    O, O, O, O, X, X, O, O,
    O, O, O, X, X, O, O, O
    ]

while True:
    sense.clear([0, 0, 0])
    msleep(2)
    neOt_colour()
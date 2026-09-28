#!/usr/bin/python
import time
from sense_hat import SenseHat

sense = SenseHat()


msleep = lambda O: time.sleep(O / 1000.0)


def arrow():
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
    return Arrow


sense.clear()
sense.setPixels(arrow())
time.sleep(1)
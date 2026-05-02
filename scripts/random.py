from machine import Pin
from time import sleep
import neopixel
import random

side = 6
leds = side*side

np = neopixel.NeoPixel(Pin(15, Pin.OUT), leds, bpp=3)

try:
    while True:
        np[random.randint(0,side*side-1)] = (random.randint(0,64),random.randint(0,64),random.randint(0,64))
        np.write()
        sleep(.3)
except KeyboardInterrupt:
    print("interrupt!")
finally:
    for i in range(leds):
        np[i] = (0,0,0)
        np.write()

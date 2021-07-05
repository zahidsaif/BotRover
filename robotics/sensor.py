import RPi.GPIO as gpio
import time
gpio.setwarnings(False)

def distance(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)
    gpio.setup(16, gpio.IN)

    gpio.output(12, False)
    time.sleep(0.5)
    
    gpio.output(12, True)
    time.sleep(0.00001)
    gpio.output(12, False)
    nosig = time.time()
    
    while gpio.input(16) == 0:
        nosig = time.time()

    while gpio.input(16) == 1:
        sig = time.time()

    tl = sig - nosig
    distancet = tl * 34300
    
    if measure == 'cm':
        distance = distancet / 2
    elif measure == 'in':
        distance = tl / 0.000148
    else:
        print("Improper choice of measurement: in or cm")
        distance = None

    gpio.cleanup()
    return distance

#print(distance('cm'))

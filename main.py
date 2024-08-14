# !/usr/bin/python
from time import sleep

from phue import Bridge
import logging
import random

if __name__ == '__main__':
    logging.basicConfig()
    b = Bridge('192.168.4.102')
    # Uncomment this line to register the app (see below)
    #b.connect()
    # Change the light state
    #b.set_light(1, 'on', False)
    print(b.get_api()['lights'])

    lights = b.lights

    # Print light names
    for l in lights:
        print(l.name + ' - ' + str(l.light_id))

    state = True

    color1 = True

    while True:
        state = not state
        #b.set_light(['Estancia1'], 'on', state)
        if color1:
            command = {'on': True, 'bri': 254, 'xy': [random.random(), random.random()]}
        else:
            command = {'on': True, 'bri': 254, 'xy': [random.random(), random.random()]}
        color1 = not color1
        b.set_group('Comedor', command)
        sleep(1)


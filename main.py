# !/usr/bin/python
from time import sleep

from phue import Bridge
import logging

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
    while True:
        state = not state
        #b.set_light(['Estancia1'], 'on', state)
        b.set_group('Comedor', 'on', state)
        sleep(3)


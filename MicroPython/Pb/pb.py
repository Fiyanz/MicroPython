from machine import Pin
from time import sleep

pb = Pin(36, Pin.IN)

while True:
    push = pb.value()
    print(f'output pb: {push}')
    if push == False:
        print('button press')
        sleep(1)
    else:
        print('nothing')
        sleep(1)

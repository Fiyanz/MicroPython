from machine import Pin
from time import sleep


listPin = [32, 33, 25, 26]
pin1 = Pin(listPin[0], Pin.OUT)
pin2 = Pin(listPin[1], Pin.OUT)
pin3 = Pin(listPin[2], Pin.OUT)
pin4 = Pin(listPin[3], Pin.OUT)

print(pin1)
print(pin2)
print(pin3)
print(pin4)

def led(nilai1, nilai2, nilai3, nilai4):
    a = pin1.value(nilai1)
    b = pin2.value(nilai2)
    c = pin3.value(nilai3)
    d = pin4.value(nilai4)
    sleep(0.2)
    print(a)
    print(b)
    print(c)
    print(d)

while True: 
    led(True, False, True, False)
    sleep(1)
    led(False, True, False, True)
    sleep(1)
   


from relay import RelayLED
from time import sleep

led = RelayLED()
while True:
    led.turnOn()
    sleep(2)
    led.turnOff()
    sleep(2)
    led.toggle()
    sleep(2)
    led.toggle()
    sleep(2)
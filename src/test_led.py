from led import TrafficLight
from led_config import config_led
from time import sleep

config = config_led()
traffic_lights = TrafficLight(*config)
sleep(2)
while True:
    traffic_lights.red_up()
    sleep(0.5)
    traffic_lights.yellow_up()
    sleep(0.5)
    traffic_lights.green_up()
    sleep(0.5)
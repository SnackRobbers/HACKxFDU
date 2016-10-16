from led import TrafficLight
from led_config import config_led
from time import sleep

config = config_led()
traffic_lights = TrafficLight(*config)
traffic_lights.all_on()
sleep(2)
try:
    while True:
        traffic_lights.red_up()
        sleep(0.5)
        traffic_lights.yellow_up()
        sleep(0.5)
        traffic_lights.green_up()
        sleep(0.5)
except KeyboardInterrupt:
    traffic_lights.all_on()
    sleep(0.5)
    traffic_lights.all_off()
    sleep(0.5)
    traffic_lights.all_on()
    sleep(0.2)
    traffic_lights.green_up()
    sleep(0.2)
    traffic_lights.yellow_up()
    sleep(0.2)
    traffic_lights.clean_up()
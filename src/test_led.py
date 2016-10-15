import led
import led_config

config = led_config()
traffic_lights = TrafficLight(*config)
traffic_lights.red_up()
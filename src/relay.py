import RPi.GPIO as GPIO

class RelayLED:
    def __init__(self, pin=7):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

        self.status = False
        self.pin = pin

    def turnOn(self):
        if self.status == False:
            GPIO.output(self.pin, GPIO.HIGH)
            self.status = not self.status

    def turnOff(self):
        if self.status == True:
            GPIO.output(self.pin, GPIO.LOW)
            self.status = not self.status

    def toggle(self):
        GPIO.output(self.pin, GPIO.LOW if self.status else GPIO.HIGH)
        self.status = not self.status

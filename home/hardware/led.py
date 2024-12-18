from machine import Pin


class LED:
    def __init__(self, pin=1):
        self.led_pin = Pin(pin, Pin.OUT)
        self.state = False
        self.off()

    def on(self):
        self.state = True
        self.led_pin.value(True)

    def off(self):
        self.state = False
        self.led_pin.value(False)

    def toggle(self):
        self.led_pin.value(not self.state)

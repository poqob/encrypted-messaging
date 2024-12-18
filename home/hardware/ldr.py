from machine import Pin


class LDR:
    def __init__(self, pin=1):
        self.ldr_pin = Pin(pin, Pin.IN)

    def read(self):
        return self.ldr_pin.value()

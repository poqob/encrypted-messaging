# display.py
from machine import SoftI2C, Pin
from home.hardware.ssd1306 import SSD1306_I2C
from time import sleep
from io import StringIO


class Display:
    def __init__(self, scl_pin=22, sda_pin=21, freq=400000, width=128, height=32):
        self.i2c = SoftI2C(
            scl=Pin(scl_pin), sda=Pin(sda_pin), freq=freq
        )  # Adjust pin numbers (5=SCL, 4=SDA) to your setup
        self.oled_width = width
        self.oled_height = height
        self.oled = SSD1306_I2C(self.oled_width, self.oled_height, self.i2c)
        st = ""
        st += "*" * 16
        st += "\n"
        st += "*" + "     POQOB    " + "*\n"
        st += "*" * 16
        self.sign = StringIO(st)

    def display(self):
        self.show(self.sign)

    def show(self, text: str, x=0, y=0):
        # self.clear()
        text = text.replace("\n", "")
        self.oled.text(text, x, y)

    def clear(self):
        self.oled.fill(0)
        self.oled.show()

    def show_stream(self, stream: StringIO):
        self.clear()
        i = 0
        while True:
            line = stream.readline()
            if not line:
                break
            self.show(line, 0, i)
            i += 10

    def show_args(self, *args):
        self.clear()
        i = 0
        for arg in args:
            self.show(arg, 0, i)
            i += 10
        self.oled.show()

# test.py
from home.methods.aes import AES
from home.communication.messages.message_manipulator import MessageManipulator
from home.hardware.hcsr04 import HCSR04


def test():
    key = b"bumBe"
    manip = MessageManipulator(AES(key=key))
    e = manip.encrypt("estonya eş genel başkanı")
    print(e.toString())
    d = manip.decrypt(e.getContent())
    print(d.getContent())


def hcsrTest():
    sensor = HCSR04(2, 4)  # trigger, echo
    value = sensor.distance_cm()
    print(value)
    # return value  # float
    return "hcsr04 test"


from machine import SoftI2C, Pin
from home.hardware.ssd1306 import SSD1306, SSD1306_I2C
from time import sleep


def display():

    # Replace -1 with SoftI2C
    i2c = SoftI2C(
        scl=Pin(22), sda=Pin(21), freq=400000
    )  # Adjust pin numbers (5=SCL, 4=SDA) to your setup
    oled_width = 128
    oled_height = 32
    oled = SSD1306_I2C(oled_width, oled_height, i2c)
    # oled.contrast(255)
    oled.text("Welcome", 0, 0)
    oled.text("ip:192.168.1.78", 0, 10)
    oled.text("data0:data0", 0, 20)
    oled.text("........................", 0, 30)
    oled.show()

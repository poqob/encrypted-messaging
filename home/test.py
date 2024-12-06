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

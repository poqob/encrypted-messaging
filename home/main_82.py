from home.connection.connection import Connection
from home.connection.socket_send import send_udp
from home.methods.aes import AES
from home.communication.messages.message_manipulator import MessageManipulator
from home.hardware.hcsr04 import HCSR04
from home.hardware.ldr import LDR

# esp32 conf
ip = "192.168.1.79"
subnet = "255.255.255.0"
gateway = "192.168.1.1"
dns = "8.8.8.8"

# aes conf
key = b"poqob&&boss"

sensor = HCSR04(2, 4)  # trigger, echo #d2,d4


def main():
    conn = Connection("merkur", "merkur.online", ip, subnet, gateway, dns)
    conn.connect()
    manipulator = MessageManipulator(AES(key=key))
    ldr = LDR(5)
    while True:
        send_udp(
            ip="192.168.1.78",
            port=7898,
            data=manipulator.encrypt(
                message=str(sensor.distance_cm())[0:7] + str(":") + str(ldr.read())
            ).getContent(),
        )

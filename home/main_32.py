from home.connection.connection import Connection
from home.connection.socket_send import (
    send_udp,
    send_udp_with_interval,
    send_tcp,
    send_tcp_with_interval,
)
from home.test import test, hcsrTest
from home.methods.aes import AES
from home.communication.messages.message_manipulator import MessageManipulator


# esp32 conf
ip = "192.168.1.79"
subnet = "255.255.255.0"
gateway = "192.168.1.1"
dns = "8.8.8.8"

# aes conf
key = b"poqob&&boss"


def main():
    conn = Connection("merkur", "merkur.online", ip, subnet, gateway, dns)
    conn.connect()
    manipulator = MessageManipulator(AES(key=key))
    send_udp_with_interval(
        ip="192.168.1.78",
        port=7898,
        data=manipulator.encrypt(message="esp32'den Esenlikler!").getContent(),
        interval=1000,
    )

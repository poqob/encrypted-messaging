# main_32.py
from home.connection.connection import Connection
from home.connection.udp_server import UDPServer
from home.connection.socket_send import (
    send_udp,
    send_udp_with_interval,
    send_tcp,
    send_tcp_with_interval,
)
from home.test import test, hcsrTest
from home.hardware.display import Display

# esp32 conf
ip = "192.168.1.78"
subnet = "255.255.255.0"
gateway = "192.168.1.1"
dns = "8.8.8.8"

# aes conf
key = b"poqob&&boss"


def main():
    conn = Connection("merkur", "merkur.online", ip, subnet, gateway, dns)
    conn.connect()
    display = Display()
    server = UDPServer(port=7898, key=key)  # -> esp32
    server.receive(display.show_args)  # -> esp32

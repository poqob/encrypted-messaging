# main_82.py
from home.connection.connection import Connection
from home.connection.udp_server import UDPServer
from home.connection.socket_send import (
    send_udp,
    send_udp_with_interval,
    send_tcp,
    send_tcp_with_interval,
)
from home.test import test, hcsrTest


# esp82 conf
ip = "192.168.1.78"
subnet = "255.255.255.0"
gateway = "192.168.1.1"
dns = "8.8.8.8"

# aes conf
key = b"poqob&&boss"


def main():
    conn = Connection("merkur", "merkur.online", ip, subnet, gateway, dns)
    conn.connect()
    server = UDPServer(port=7898, key=key)  # -> esp82
    server.receive()  # -> esp82

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
"""
ip = "192.168.1.78"
subnet = "255.255.255.0"
gateway = "192.168.1.1"
dns = "8.8.8.8"  
"""

# esp32 conf
ip = "192.168.1.79"
subnet = "255.255.255.0"
gateway = "192.168.1.1"
dns = "8.8.8.8"
if __name__ == "__main__":
    conn = Connection("merkur", "merkur.online", ip, subnet, gateway, dns)
    conn.connect()
    # test()
    # server = UDPServer() -> esp82
    # server.receive() -> esp82
    # hcsrTest() -> esp32
    send_udp_with_interval(ip=ip, port=8080, data="Hello, world!", interval=1000)

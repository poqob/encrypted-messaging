from home.connection.get_mac import wifi_connect
from home.connection.connection import Connection
from home.connection.espnow_receiver import receiver
from home.connection.espnow_sender import sender
import gc
from home.test import test, hcsrTest


ip = "192.168.1.100"
subnet = "255.255.255.0"
gateway = "192.168.1.1"
dns = "8.8.8.8"
if __name__ == "__main__":
    conn = Connection("merkur", "merkur.online", ip, subnet, gateway, dns)
    conn.connect()
    test()
    # hcsrTest()

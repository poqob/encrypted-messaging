from home.connection.connection import Connection
from home.main_32 import main

# from home.main_82 import main

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
    main()

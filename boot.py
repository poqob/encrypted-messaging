# This file is executed on every boot (including wake-boot from deepsleep)

# import esp

# esp.osdebug(None)

import os
import machine
import time

from home.connection.get_mac import wifi_connect


import gc

from home.test import test


def receiver():
    import network
    import espnow

    # A WLAN interface must be active to send()/recv()
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.disconnect()  # Because ESP8266 auto-connects to last Access Point

    e = espnow.ESPNow()
    e.active(True)

    while True:
        host, msg = e.recv()
        if msg:  # msg == None if timeout in recv()
            print(host, msg)
            if msg == b"end":
                break


def sender():
    # espnow_sender.py || esp32
    import network
    import espnow

    # A WLAN interface must be active to send()/recv()
    sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
    sta.active(True)
    sta.disconnect()  # For ESP8266

    e = espnow.ESPNow()
    e.active(True)
    # peer = b'\xbb\xbb\xbb\xbb\xbb\xbb'   # MAC address of peer's wifi interface
    peer = b"\x30\x83\x98\xb6\x3e\x24"
    e.add_peer(peer)  # Must add_peer() before send()

    e.send(peer, "Starting...")
    for i in range(100):
        e.send(peer, str(i) * 20, True)
    e.send(peer, b"end")

    # esp 8266 mac: 30:83:98:B6:3E:24
    # hex to bytes: peer = b'\x30\x83\x98\xb6\x3e\x24'


if __name__ == "__main__":
    # wifi_connect('merkur','merkur.online')
    sender()

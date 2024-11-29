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

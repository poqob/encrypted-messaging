# get_mac.py
def wifi_connect(ssid, pwd):
    sta_if = None
    import network

    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, pwd)
        while not sta_if.isconnected():
            pass
    print("----------------------------------------")
    print("network config:", sta_if.ifconfig())
    print("----------------------------------------")

    get_my_mac_addr(sta_if)


def get_my_mac_addr(sta_if):
    import ubinascii
    import network

    wlan_mac = sta_if.config("mac")
    my_mac_addr = ubinascii.hexlify(wlan_mac).decode()

    my_mac_addr = format_mac_addr(my_mac_addr)


def format_mac_addr(addr):

    mac_addr = addr
    mac_addr = mac_addr.upper()

    new_mac = ""

    for i in range(0, len(mac_addr), 2):
        # print(mac_addr[i] + mac_addr[i+1])

        if i == len(mac_addr) - 2:
            new_mac = new_mac + mac_addr[i] + mac_addr[i + 1]
        else:
            new_mac = new_mac + mac_addr[i] + mac_addr[i + 1] + ":"
    print("----------------------------------------")
    print("My MAC Address:" + new_mac)
    print("----------------------------------------")
    return new_mac

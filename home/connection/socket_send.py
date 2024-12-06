# socket_send.py
import socket
import time


def send_tcp(data="", ip="", port=None):
    sockaddr = socket.getaddrinfo(ip, port)[0][-1]
    s = socket.socket()
    s.connect(sockaddr)
    s.send(data)
    print(f"Sent data: {data}")
    s.close()


def send_udp(data="", ip="", port=None):
    sockaddr = socket.getaddrinfo(ip, port)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(data, sockaddr)
    print(f"Sent data: {data}")
    s.close()


def send_udp_with_interval(data="", ip="", port=None, interval=1000):
    while True:
        send_udp(data, ip, port)
        time.sleep(interval / 1000)


def send_tcp_with_interval(data="", ip="", port=None, interval=1000):
    while True:
        send_tcp(data, ip, port)
        time.sleep(interval / 1000)

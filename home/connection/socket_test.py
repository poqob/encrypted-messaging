# socket_test.py


import socket
import time


def test(data="", chunk_size=4):
    sockaddr = socket.getaddrinfo("192.168.147.224", 65432)[0][-1]
    print(sockaddr)
    s = socket.socket()
    s.connect(sockaddr)
    chunks = [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]

    for chunk in chunks:
        s.send(chunk.encode("utf-8"))
        print(f"Sent chunk: {chunk}")
        time.sleep(1)


def send(data="", ip="", port=None):
    sockaddr = socket.getaddrinfo(ip, port)[0][-1]
    s = socket.socket()
    s.connect(sockaddr)
    s.send(data.encode("utf-8"))
    print(f"Sent data: {data}")
    s.close()

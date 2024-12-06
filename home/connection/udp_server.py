# udp_server.py
import socket


class UDPServer:
    def __init__(self, ip="0.0.0.0", port=8080):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # <-- udp
        self.udp_socket.bind((ip, port))  # Listen on all interfaces, port 8080
        self.port = port
        self.ip = ip

    def receive(self):
        try:
            while True:
                # Receive data and the client's address
                data, client_address = self.udp_socket.recvfrom(
                    1024
                )  # Buffer size is 1024 bytes
                print(
                    "Received from {}: {}".format(client_address, data.decode("utf-8"))
                )
                # Respond to the client (optional)
                self.udp_socket.sendto(b"Data received!", client_address)
        except KeyboardInterrupt:
            print("Server stopped.")
        finally:
            self.udp_socket.close()

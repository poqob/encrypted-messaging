# udp_server.py
import socket
from home.methods.aes import AES
from home.communication.messages.message_manipulator import MessageManipulator


class UDPServer:
    def __init__(self, ip="0.0.0.0", port=8080, key="key"):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # <-- udp
        self.udp_socket.bind((ip, port))  # Listen on all interfaces, port 8080
        self.port = port
        self.ip = ip
        self.manipulator = MessageManipulator(AES(key=key))

    def receive(self):
        try:
            while True:
                # Receive data and the client's address
                data, client_address = self.udp_socket.recvfrom(
                    1024
                )  # Buffer size is 1024 bytes

                resolved_data = self.manipulator.decrypt(data.decode("utf-8"))

                print(
                    "Received from {}: {}".format(client_address, data.decode("utf-8"))
                )

                print("Resolved: {}".format(resolved_data.getContent()))

        except KeyboardInterrupt:
            print("Server stopped.")
        finally:
            self.udp_socket.close()

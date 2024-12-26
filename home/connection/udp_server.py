# udp_server.py
import socket
from home.methods.aes import AES
from home.methods.ceaser import Ceaser
from home.communication.messages.message_manipulator import MessageManipulator
from home.hardware.led import Led


class UDPServer:
    def __init__(self, ip="0.0.0.0", port=8080, key="key"):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # <-- udp
        self.udp_socket.bind((ip, port))  # Listen on all interfaces, port 8080
        self.port = port
        self.ip = ip
        self.manipulator = MessageManipulator(AES(key=key))
        self.led = Led(13)

    def receive(self, callback):
        try:
            while True:
                # Receive data and the client's address
                data, client_address = self.udp_socket.recvfrom(
                    1024
                )  # Buffer size is 1024 bytes

                resolved_data = self.manipulator.decrypt(data)
                resolved_data_as_str = resolved_data.content
                print("Received data:{}\nReceived from:{}".format(data, client_address))

                callback(
                    "srv:{}:{}\n".format(self.ip, self.port),
                    "cln:{}\n".format(client_address[0]),
                    "data:{}".format(resolved_data_as_str),
                )

                if resolved_data_as_str[-1] == "0":
                    self.led.on()
                else:
                    self.led.off()

        except KeyboardInterrupt:
            print("Server stopped.")
        finally:
            self.udp_socket.close()

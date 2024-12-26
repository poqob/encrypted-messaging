# message_manipulator.py
from home.methods.a_method import AMethod
from home.communication.messages.message_object import MessageObject
from home.methods.ceaser import Ceaser


class MessageManipulator:
    def __init__(self, method: AMethod):
        self.method = method
        self.ceaser = Ceaser(3)

    def encrypt(self, message: str) -> MessageObject:
        message = self.ceaser.encrypt(message)
        result = self.method.encrypt(message)
        return MessageObject(result)

    def decrypt(self, message: str) -> MessageObject:
        message = self.method.decrypt(message)
        result = self.ceaser.decrypt(message)
        return MessageObject(result)

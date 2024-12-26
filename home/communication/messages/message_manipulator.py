# message_manipulator.py
from home.methods.a_method import AMethod
from home.communication.messages.message_object import MessageObject


class MessageManipulator:
    def __init__(self, method: AMethod):
        self.method = method

    def encrypt(self, message: str) -> MessageObject:
        result = self.method.encrypt(message)
        return MessageObject(result)

    def decrypt(self, message: str) -> MessageObject:
        result = self.method.decrypt(message)
        return MessageObject(result)

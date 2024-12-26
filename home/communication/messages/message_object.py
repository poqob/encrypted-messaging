# message_object.py
class MessageObject:
    def __init__(self, message: str):
        self.content = message

    def getContent(self):
        return self.content

    def __str__(self):
        return self.content

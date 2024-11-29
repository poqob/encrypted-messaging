from home.methods.aes import AES
from home.communication.messages.message_manipulator import MessageManipulator


def test():
    key = b"bumBe"
    manip = MessageManipulator(AES(key=key))
    e = manip.encrypt("metin")
    print(e.getContent())
    d = manip.decrypt(e.getContent())
    print(d.getContent())

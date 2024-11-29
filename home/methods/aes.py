# Aes.py
from cryptolib import aes
import os

# key and message are padded with pkcs7 alghorithm.
# message object: iv + message (cyrpted)
from home.methods.a_method import AMethod


class AES(AMethod):
    def __init__(self, key: bytes):  # embeded 16bytes long key
        self.key = self.pkcs7_pad(key)

    def pkcs7_pad(self, data: bytes, block_size: int = 16) -> bytes:
        padding_len = block_size - (len(data) % block_size)
        padding = bytes([padding_len] * padding_len)
        return data + padding

    def pkcs7_unpad(self, padded_data: bytes) -> bytes:
        padding_len = padded_data[-1]
        return padded_data[:-padding_len]

    def encrypt(self, message: str) -> str:
        message_bytes = message.encode("utf-8")  # Convert message to bytes
        padded = self.pkcs7_pad(data=message_bytes)

        iv = os.urandom(16)
        result = iv + padded
        cipher = aes(self.key, 2, iv)
        ciphertext = cipher.encrypt(result)
        return ciphertext

    def decrypt(self, message: str) -> str:
        iv = message[:16]
        content = message[16:]
        cipher = aes(self.key, 2, iv)
        decrypted = cipher.decrypt(content)
        decrypted = self.pkcs7_unpad(decrypted)
        plaintext = decrypted.decode("utf-8")
        return plaintext

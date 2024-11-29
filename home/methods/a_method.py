# a_method.py
class AMethod:
    def encrypt(self, data: str) -> str:
        raise NotImplementedError("Subclasses must implement encrypt()")

    def decrypt(self, data: str) -> str:
        raise NotImplementedError("Subclasses must implement decrypt()")

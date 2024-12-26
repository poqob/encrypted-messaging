class Ceaser:
    def __init__(self, shift=0):
        self.shift = shift
        self.dynamic = self.shift == 0

    def encrypt(self, data):
        if self.dynamic:
            self.shift = len(data)
        result = []
        for char in data:
            if (
                isinstance(char, str) and len(char) == 1
            ):  # Ensure char is a single character
                if "A" <= char <= "Z":  # Check for uppercase letters
                    result.append(chr((ord(char) + self.shift - 65) % 26 + 65))
                elif "a" <= char <= "z":  # Check for lowercase letters
                    result.append(chr((ord(char) + self.shift - 97) % 26 + 97))
                else:
                    result.append(char)  # Leave non-alphabetic characters unchanged
            else:
                result.append(str(char))  # Convert other types to string
        return "".join(result)

    def decrypt(self, data):
        if self.dynamic:
            self.shift = len(data)
        result = []
        for char in data:
            if (
                isinstance(char, str) and len(char) == 1
            ):  # Ensure char is a single character
                if "A" <= char <= "Z":  # Check for uppercase letters
                    result.append(chr((ord(char) - self.shift - 65) % 26 + 65))
                elif "a" <= char <= "z":  # Check for lowercase letters
                    result.append(chr((ord(char) - self.shift - 97) % 26 + 97))
                else:
                    result.append(char)  # Leave non-alphabetic characters unchanged
            else:
                result.append(str(char))  # Convert other types to string
        return "".join(result)

    def __str__(self):
        return "Ceaser Cipher with shift {}".format(self.shift)

from Crypto.Cipher import AES


class CryptoSystem:
    def __init__(self, key):
        self.key = key
        self.encipher = AES.new(key, AES.MODE_EAX)
        self.decipher = AES.new(key, AES.MODE_EAX, nonce=self.encipher.nonce)

    def encrypt(self, text: str):
        ciphertext, tag = self.encipher.encrypt_and_digest(text.encode('utf-8'))
        return ciphertext, tag

    def decrypt(self, ciphertext, tag):
        plaintext = self.decipher.decrypt(ciphertext)
        try:
            self.decipher.verify(tag)
        except ValueError:
            print("Key incorrect or message corrupted")
        return plaintext


if __name__ == "__main__":
    text = "ab"
    cs = CryptoSystem(b'Sixteen byte key')
    c, t = cs.encrypt(text)
    print(c)
    print(cs.decrypt(c, t))

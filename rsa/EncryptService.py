
from typing import Final
import Crypto
from Crypto import PublicKey
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


class EncryptService:
    __PRIVATE_KEY: Final = b''
    
    __PUBLIC_KEY: Final = b''

    def encrypt(self, data: str):
        publicKey: Final = RSA.import_key(self.__PUBLIC_KEY)
        encryptor = PKCS1_OAEP.new(publicKey)
        return base64.b64encode(encryptor.encrypt(str.encode(data))).decode()
    
    def decrypt(self, data: str):
        msg = base64.b64decode(str.encode(data))
        privateKey = RSA.import_key(self.__PRIVATE_KEY)
        decryptor = PKCS1_OAEP.new(privateKey)
        return decryptor.decrypt(msg).decode('utf-8')        
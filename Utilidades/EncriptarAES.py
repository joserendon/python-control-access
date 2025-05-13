import binascii;
from Crypto.Cipher import AES;
class EncriptarAES:
    secretKey = b'\xa8\xb3\x1f\xc2\x4d\xf6\x98\x12\xd4\xab\xc9\xb7Z\xee\xd0X\x1e\x8b\x99q\x2a\xf0C\x9e\xad4\xbd\x7f\x91\xb1\xe6\xe0'    
    
    def Cifrar(self, valor: str) -> str:
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM);
        ciphertext, authTag = aesCipher.encrypt_and_digest(str.encode(valor));
        response = (ciphertext, aesCipher.nonce, authTag);
        return binascii.hexlify(response[0]).decode() + '|' + binascii.hexlify(response[1]).decode() + '|' + binascii.hexlify(response[2]).decode();

    def Decifrar(self, valor: str) -> str:
        split = valor.split('|');
        ciphertext = binascii.unhexlify(split[0]);
        nonce = binascii.unhexlify(split[1]);
        authTag = binascii.unhexlify(split[2]);
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce);
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag);
        return plaintext.decode();
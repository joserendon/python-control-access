
import hashlib
import os
import base64
import hmac

class PasswordHash:
    ITERATIONS = 310_000
    HASH_NAME = 'sha512'  
    KEY_LENGTH = 32 
    SALT_LENGTH = 16
    
    
    # Hashear una contraseña
    def hash_password(self, password: str) -> str:
        salt = os.urandom(self.SALT_LENGTH)
        dk = hashlib.pbkdf2_hmac(self.HASH_NAME, password.encode(), salt, self.ITERATIONS, dklen=self.KEY_LENGTH)
        # Almacenar en formato base64: salt$hash
        return f"{base64.b64encode(salt).decode()}${base64.b64encode(dk).decode()}"

    # Verificar una contraseña contra un hash almacenado
    def verify_password(self, password: str, stored: str) -> bool:
        salt_b64, hash_b64 = stored.split('$')
        salt = base64.b64decode(salt_b64)
        stored_hash = base64.b64decode(hash_b64)
        new_hash = hashlib.pbkdf2_hmac(self.HASH_NAME, password.encode(), salt, self.ITERATIONS, dklen=self.KEY_LENGTH)
        return hmac.compare_digest(stored_hash, new_hash)
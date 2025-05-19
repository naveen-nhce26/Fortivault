from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_file(file_bytes: bytes) -> bytes:
    return cipher.encrypt(file_bytes)

def decrypt_file(encrypted_bytes: bytes) -> bytes:
    return cipher.decrypt(encrypted_bytes)

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii
import random

def aes_encrypt(data, key):
    iv = bytes([random.randint(0, 255) for _ in range(16)]) 
    if len(key)!=32:
        return "key should be of 32 bytes"
    encrypted_bytes = AES.new(key.encode(), AES.MODE_CBC, iv)
    padded_data = pad(data.encode(), AES.block_size)
    encrypted_data = encrypted_bytes.encrypt(padded_data)
    encrypted_iv_data = iv + encrypted_data
    hex_encrypted_iv_data = binascii.hexlify(encrypted_iv_data).decode()
    
    return hex_encrypted_iv_data

def aes_decrypt(hex_encrypted_iv_data, key):
    encrypted_iv_data = binascii.unhexlify(hex_encrypted_iv_data)
    iv = encrypted_iv_data[:16]
    encrypted_data = encrypted_iv_data[16:]
    if len(key) != 32:
        return "Key should be of 32 bytes"
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    data = unpad(decrypted_data, AES.block_size).decode()
    
    return data
from pyDes import des, CBC, PAD_PKCS5
import binascii
import random
import sys

def des_encrypt(plain_text, key):
    iv = bytes([random.randint(0, 255) for _ in range(8)])
    if len(key) != 8:
        return "The key must be 8 bytes long"
    encrypted_bits = des(key, CBC, iv, padmode=PAD_PKCS5)
    encrypted_data = encrypted_bits.encrypt(plain_text.encode())
    encrypted_iv_data = iv + encrypted_data
    encryption = binascii.hexlify(encrypted_iv_data).decode()
    return encryption

def des_decrypt(encryption, key):
    encrypted_iv_data = binascii.unhexlify(encryption)
    iv = encrypted_iv_data[:8]
    encrypted_data = encrypted_iv_data[8:]
    if len(key) != 8:
        return "The key must be 8 bytes long"
    else:
        try:
            cipher_for_decryption = des(key, CBC, iv, padmode=PAD_PKCS5)
            decrypted_data = cipher_for_decryption.decrypt(encrypted_data)
            plain_text = cipher_for_decryption.no_pad(decrypted_data).decode()
            return plain_text
        except Exception as e:
            return f'Something went wrong: {e}'

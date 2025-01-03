from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Function to generate RSA keys (public and private)
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Function to encrypt data using RSA public key
def rsa_encrypt(plain_text, public_key):
    public_key_obj = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(public_key_obj)
    encrypted_data = cipher.encrypt(plain_text.encode())
    return binascii.hexlify(encrypted_data).decode()

def rsa_decrypt(hex_encrypted_data, private_key):
    private_key_obj = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private_key_obj)
    encrypted_data = binascii.unhexlify(hex_encrypted_data)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode()




import hashlib

def sha256_hash(plain_text):
    sha256 = hashlib.sha256()
    sha256.update(plain_text.encode())
    return sha256.hexdigest()
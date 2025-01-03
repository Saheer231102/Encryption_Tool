import base64

def base64_encode(plain_text):
    encoded_bytes = base64.b64encode(plain_text.encode())
    return encoded_bytes.decode()

def base64_decode(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text)
    return decoded_bytes.decode()
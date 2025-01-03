def ceaser_encrypt(plaintext, key):
    result = ""
    for i in plaintext:
        if ord(i) >=97 and ord(i)<=122:
            result += chr(ord(i) +key)
        elif ord(i)>=65 and ord(i)<=90:
            result += chr(ord(i) +key)
        else:
            result += i

    return result

def ceaser_decrypt(encrypted, key):
    result = ""
    for i in encrypted:
        if ord(i) >=97 and ord(i)<=122:
            result += chr(ord(i) -key)
        elif ord(i)>=65 and ord(i)<=90:
            result += chr(ord(i) -key)
        else:
            result += i

    return result

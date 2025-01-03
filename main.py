import ceaser
import aes
import desalgo
import rsa
import sha
import bse64

print("""------------------------------------WELCOmE TO THE CRYPTOGRAPHY TOOL------------------------------------
NOTE: This tool contains only 6 types of encoding, encryption, hashing algorithm. If you find what you want enjoy :)""")

while True:
    user_first_input = int(input("What type of algorithm would you like to utilize now?\n1. Encryption / Decryption\n2. Encoding / Decoding\n3. Hashing\n>"))
    
    if(user_first_input == 1):
        user_second_input = int(input("Which of these would you like to utilize?\n1. Ceaser Cipher\n2. AES\n3. DES\n4. RSA\nRefer README for more info on these methods.\n>"))
        if(user_second_input == 1):
            user_third_input = int(input("What would you like to do\n1. Encryption\n2. Decyrption\n>"))
            if(user_third_input == 1):
                text = input("Enter plain text you want to encrypt:\n>")
                key = int(input("Enter key that you would like to utilize[any numeric value]:\n>"))
                print(f"OUTPUT: {ceaser.ceaser_encrypt(text, key)}")
            elif(user_third_input == 2):
                text = input("Enter encrypted text you want to decrypt:\n>")
                key = int(input("Enter key that you had utilized to encrypt[numeric value used as key]\n>"))
                print(f"OUTPUT : {ceaser.ceaser_decrypt(text,key)}")
            else:
                print("Please select a valid option\n")
        elif(user_second_input == 2):
            user_third_input = int(input("What would you like to do\n1. Encryption\n2. Decyrption\n>"))
            if(user_third_input == 1):
                text = input("Enter plain text you want to encrypt:\n>")
                key = input("Enter key that you would like to utilize[32 bytes value]:\n>")
                print(f"OUTPUT: {aes.aes_encrypt(text,key)}")
            elif(user_third_input == 2):
                text = input("Enter encrypted text you want to decrypt:\n>")
                key = input("Enter key that you had utilized to encrypt[32 bytes value]\n>")
                print(f"OUTPUT : {aes.aes_decrypt(text,key)}")
            else:
                print("Please select a valid option\n")
        elif(user_second_input == 3):
            user_third_input = int(input("What would you like to do\n1. Encryption\n2. Decyrption\n>"))
            if(user_third_input == 1):
                text = input("Enter plain text you want to encrypt:\n>")
                key = int(input("Enter key that you would like to utilize[8 bytes value]:\n>"))
                print(f"OUTPUT: {desalgo.des_encrypt(text,key)}")
            elif(user_third_input == 2):
                text = input("Enter encrypted text you want to decrypt:\n>")
                key = int(input("Enter key that you had utilized to encrypt[8 bytes value]\n>"))
                print(f"OUTPUT : {desalgo.des_decrypt(text,key)}")
            else:
                print("Please select a valid option\n")
        elif(user_second_input == 4):
            user_third_input = int(input("Do you have the rsa keys?[y or n]\n>"))
            if(user_third_input.lower() == 'y'):
                user_fourth_input = int(input("What would you like to do\n1. Encryption\n2. Decyrption\n>"))
                if(user_fourth_input == 1):
                    text = input("Enter plain text you want to encrypt:\n>")
                    key = int(input("Enter The public key\n>"))
                    print(f"OUTPUT: {rsa.rsa_encrypt(text,key)}")
                elif(user_fourth_input == 2):
                    text = input("Enter encrypted text you want to decrypt:\n>")
                    key = int(input("Enter your private key\n>"))
                    print(f"OUTPUT : {rsa.rsa_decrypt(text,key)}")
                else:
                    print("Please select a valid option\n")
            elif(user_third_input.lower()=='n'):
                print("GENERATING RSA KEYS FOR YOU!")
                public_key, private_key = rsa.generate_rsa_keys()
                print("PUBLIC KEY IS", public_key,"\n")
                print("PRIVATE KEY IS", private_key,"\n")
                user_fourth_input = int(input("What would you like to do\n1. Encryption\n2. Decyrption\n>"))
                if(user_fourth_input == 1):
                    text = input("Enter plain text you want to encrypt:\n>")
                    print(f"OUTPUT: {rsa.rsa_encrypt(text,public_key)}")
                elif(user_fourth_input == 2):
                    text = input("Enter encrypted text you want to decrypt:\n>")
                    print(f"OUTPUT : {rsa.rsa_decrypt(text,private_key)}")
                else:
                    print("Please select a valid option\n")
            else: 
                print("Please select a valid option\n")
        else:
            print("Please enter a valid option\n")
    elif(user_first_input == 2):
        print("Only Base64 Encoding is avilable choosing Base64 by default.\n")
        user_third_input = int(input("What would you like to do\n1. Encoding\n2. Decoding\n>"))
        if(user_fourth_input == 1):
            text = input("Enter plain text you want to encode:\n>")
            print(f"OUTPUT: {bse64.base64_encode(text)}")
        elif(user_fourth_input == 2):
            text = input("Enter encoded text you want to decode:\n>")
            print(f"OUTPUT : {bse64.base64_decode(text)}")
        else:
            print("Please select a valid option")
    elif(user_first_input == 3):
        print("Only sha-256 Hashing is available choosing SHA-256 by default.\nSO.. Hashing is one way it only encyrpts stuff. Just for your info.\n")
        text = input("Enter plain text you want to encode:\n>")
        print("OUTPUT : ", sha.sha256_hash(text),"\n")
    else:
        print("Please choose a valid option!\n")
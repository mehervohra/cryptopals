import os
import random
import Challenge210
import Challenge17
import Challenge18

def genBytes():
    return os.urandom(16)

def encryption_oracle(plaintext):
    key = genBytes()
    plaintext = os.urandom(random.randint(5, 10)) + plaintext.encode("utf-8") + os.urandom(random.randint(5, 10))
    method = random.randint(0, 1)
    
    if method == 0:
        iv = os.urandom(16)
        return Challenge210.encryptCBC(plaintext, key, iv)
    else:
        numBlocks = int(len(plaintext) / 16)
        ciphertext = b''
        for i in range(numBlocks):
            block = plaintext[i*16: (i+1)*16]
            ciphertext+= Challenge17.encrypt(block, key)
        return ciphertext

def detectMethod(ciphertext):
    if Challenge18.isECB(ciphertext):
        return "ECB"
    else:
        return "CBC"

print(detectMethod(encryption_oracle("this is a test string for encryption okay")))

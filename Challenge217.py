#THIS IS INCOMPLETE

from Crypto.Cipher import AES
import os
import Challenge29
import Challenge215

key = os.urandom(16)

def encrypt(plaintext):
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv, cipher.encrypt(Challenge29.pkcsPadding(plaintext))

def validPadding(ciphertext, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return Challenge215.validPKCS(plaintext)

def readStrings():
    seventeen = open("seventeen.txt", "r")
    for item in seventeen:
        ciphertext = encrypt(item)
        print(validPadding(ciphertext))

readStrings()
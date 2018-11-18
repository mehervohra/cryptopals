import os
import Challenge29
import Challenge210
import Challenge12
from Crypto.Cipher import AES

key = os.urandom(16)
iv = os.urandom(16)
cipher = AES.new(key, AES.MODE_CBC, iv)

def setUp(s, BLOCKSIZE=16):
    concatenated = "comment1=cooking%20MCs;userdata=" + s + ";comment2=%20like%20a%20pound%20of%20bacon"
    noQuotes = concatenated.replace(";", "")
    noEquals = noQuotes.replace("=", "")
    padded = Challenge29.pkcsPadding(noEquals, BLOCKSIZE)
    encrypted = cipher.encrypt(padded.encode())
    return encrypted

# print(setUp("hello"))

def decryptAttempt(ciphertext):
    decrypted = cipher.decrypt(ciphertext)
    return b';admin=true;' in decrypted
         
# print(decryptAttempt(setUp("hello")))

def realAttempt(ciphertext):
    toReplace = ciphertext[32:48]
    nextB = Challenge12.fixedXORs(b';comment2=%20lik', toReplace)
    evilB = Challenge12.fixedXORs(b';admin=true;aaaa', nextB)
    total = ciphertext[:32] + evilB + ciphertext[32:]
    return total
    
# ciphertext = setUp("sixteenejrekr")
# hijacked = realAttempt(ciphertext)
# print(decryptAttempt(hijacked))
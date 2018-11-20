#THIS IS INCOMPLETE

import os
from Crypto.Cipher import AES
import Challenge29
import random
import base64

key = os.urandom(16)
random = os.urandom(random.randint(0, 32))

after = base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
cipher = AES.new(key, AES.MODE_ECB)

def encryption_oracle(plaintext):
    plaintext = random + plaintext.encode() + after
    padded = Challenge29.pkcsPadding(plaintext)
    return cipher.encrypt(padded)
    
def cipherBlocksize():
    ciphertext = encryption_oracle("")
    originalSize = len(ciphertext)
    size = len(ciphertext)
    i=1
    while size == originalSize:
        ciphertext = encryption_oracle("A" * i)
        size = len(ciphertext)
        i+=1
    return size - originalSize

# print(encryption_oracle("hello this is encryption"))
# print(cipherBlocksize())
print(byteAtTimeDec())
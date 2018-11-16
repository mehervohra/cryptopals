import os
from Crypto.Cipher import AES
import Challenge29
import Challenge18
import base64

key = os.urandom(16)

after = base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
cipher = AES.new(key, AES.MODE_ECB)

def encryption_oracle(plaintext):
    plaintext = plaintext.encode() + after
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

def checkECB():
    return Challenge18.isECB(encryption_oracle(""))

def byteAtTimeDec():
    decoded = ""
    block_size = cipherBlocksize()
    allPossibleBytes = bytes([x for x in range(0xFF+1)])
    for block in range(int(len(after)/block_size)):
        for i in range(block_size-1):
        # for i in range(3):
            # print(cipher.decrypt(encryption_oracle((block_size-i-1)*"A"+decoded)[0*16:1*16]))
            # print("round: " + str(block_size-i-1) + " decoded " + decoded)
            ciphertext = encryption_oracle((block_size-i-1)*"A")[block*block_size : (block+1)*block_size]
            # print(cipher.decrypt(ciphertext))

            for byte in allPossibleBytes:
                tempCipher = encryption_oracle((block_size-i-1)*"A" + decoded + chr(byte))[0:block_size]
                if (ciphertext==tempCipher):
                    decoded += chr(byte)
                    break
    return decoded

# print(encryption_oracle("hello this is encryption"))
# print(cipherBlocksize())
# print(checkECB())
# print(byteAtTimeDec())
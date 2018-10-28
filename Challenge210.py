import Challenge12
import base64
import Challenge17
from Crypto.Cipher import AES

def encryptCBC(message, key, iv):
    BLOCK_SIZE = 16
    previous = iv
    ciphertext = b''
    numBlocks = int(len(message) / BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_ECB)

    for i in range(numBlocks):
        xor = Challenge12.fixedXORs(message[i*BLOCK_SIZE: (i+1)*BLOCK_SIZE], previous)
        encrypted = cipher.encrypt(xor) 
        previous = encrypted
        ciphertext += encrypted
    return encrypted
     
def decryptCBC(ciphertext, key, iv):
    previous = iv
    BLOCK_SIZE = 16
    numBlocks = int(len(ciphertext) / BLOCK_SIZE)
    message = ""
    for i in range(numBlocks):
        current = ciphertext[i*BLOCK_SIZE : (i+1)*BLOCK_SIZE]
        decrypted = Challenge17.decrypt(current, key)
        xor = Challenge12.fixedXORs(decrypted, previous)
        previous = current
        message += xor.decode()
    return message

with open ("ten.txt") as ten:
    ciphertext = base64.b64decode(ten.read().strip())
    iv = b'\x00'*16
    key = "YELLOW SUBMARINE"
    encrypted = encryptCBC(b'encryption message', key, iv)
    print(encrypted)
    print(decryptCBC(encrypted, key, iv))
    # print(decryptCBC(ciphertext, "YELLOW SUBMARINE", iv))
    
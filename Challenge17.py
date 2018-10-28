from Crypto.Cipher import AES
import base64

def encrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(ciphertext)
    
def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)
    
with open ("seven.txt") as seven:
    ciphertext = base64.b64decode(seven.read())
    key = 'YELLOW SUBMARINE'
    print(decrypt(ciphertext, key))
    
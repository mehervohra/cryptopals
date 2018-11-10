
def validPKCS(plaintext, BLOCKSIZE=16):
    if type(plaintext) == str:
        plaintext = plaintext.encode()
    last = plaintext[-1]

    if last!=0 and plaintext[-last:]==bytes(last*[last]):
        length = len(plaintext)-last
        return plaintext[:length].decode()
    return False

# print(validPKCS("ICE ICE BABY\x04\x04\x04\x04"))
# print(validPKCS("ICE ICE BABY\x05\x05\x05\x05"))
# print(validPKCS("ICE ICE BABY\x01\x02\x03\x04"))

print(validPKCS("email=foo@bar.com&uid=7&role=user\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f"))
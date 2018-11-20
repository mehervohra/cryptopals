#THIS IS INCOMPLETE

def hammingDistance(s1, s2):
    result = 0
    for byte1, byte2 in zip(s1, s2):
        xor = byte1 ^ byte2
        for b in bin(xor):
            if b == '1':
                result += 1
    return result

print(hammingDistance(b'this is a test', b'wokka wokka!!!'))

sixList = open("six.txt", "r")
for item in sixList:
    pass

def breakXOR(message):    
    for keysize in range(2, 40):
        sub1 = message[:keysize]
        sub2 = message[keysize:keysize*2]
        dist = hammingDistance(sub1, sub2)
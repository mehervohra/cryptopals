import codecs
import Challenge12

def singleByteXOR(input):
    allBytes = bytes([x for x in range(0xFF+1)])
    key = b'-1'
    maxScore = 0
    maxMessage = b'-1'
    letterFreq = {'e': 12.02, 't': 9.10, 'a': 8.12, 'o': 7.31, 'i': 7.31, 'n': 6.95, 's': 6.28,
        'h': 5.92, 'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36,
        'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15,
        'x': 0.15, 'q': 0.10, 'z': 0.07}
    allLetters = b"abcdefghijklmnopqrstuvwxyz"
    for b in allBytes:
        fullByte = str(b)*len(input)
        xor = Challenge12.fixedXORs(codecs.decode(input, "hex"), codecs.decode(fullByte, "hex"))
        currentScore = 0
        for letter in xor.lower():
            if letter in allLetters:
                currentScore+= letterFreq[chr(letter)]
        if currentScore > maxScore:
            maxScore = currentScore
            key = b
            maxMessage = xor
    return key, maxMessage, maxScore
    
print(singleByteXOR('0e3647e8592d35514a081243582536ed3de6734059001e3f535ce6271032'))
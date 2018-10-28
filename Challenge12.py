import codecs

def fixedXORs(buf1, buf2):
    return codecs.encode(bytes([b1 ^ b2 for (b1, b2) in zip(buf1, buf2)]), "hex")
    
buf1 = codecs.decode('1c0111001f010100061a024b53535009181c', "hex")
buf2 = codecs.decode('686974207468652062756c6c277320657965', "hex")
print(fixedXORs(buf1, buf2))
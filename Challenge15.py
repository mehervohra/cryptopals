import codecs

def repeatKeyXOR(key, message):
    result = b''
    i = 0
    for letter in message:
        result += bytes([letter ^ key[i]])
        if (i == (len(key) - 1)):
            i = 0
        else:
            i += 1
    return codecs.encode(result, "hex")

print(repeatKeyXOR(b'ICE', b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"))
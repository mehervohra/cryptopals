import base64
import codecs
def hexToBase64(input):
    string = codecs.decode(input, "hex")
    return base64.b64encode(string)

print(hexToBase64(b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
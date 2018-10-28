
def pkcsPadding(message, blocksize):
    if len(message) >= blocksize:
        paddingSize = len(message) % blocksize
    else:
        paddingSize = blocksize % len(message)
    if (paddingSize != 0):
        message += paddingSize*str(bytes([paddingSize]))
    return message
        
print(pkcsPadding("YELLOW SUBMARINE", 20))
  
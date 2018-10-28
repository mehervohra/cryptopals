import base64

def isECB(ciphertext):
    BLOCK_SIZE = 16
    numBlocks = int(len(ciphertext) / BLOCK_SIZE)
    for i in range(numBlocks):
        for j in range(i+1, numBlocks):
            if ciphertext[i*BLOCK_SIZE : (i+1)*BLOCK_SIZE] == ciphertext[j*BLOCK_SIZE : (j+1)*BLOCK_SIZE]: #if currentBlock is equal to another block it is probs ECB
                return True
    return False           

eightList = open("eight.txt", "r")
for item in eightList:
    item = item.strip()
    if isECB(base64.b64decode(item)):
        print(item)
        
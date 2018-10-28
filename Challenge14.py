import Challenge13

fourList = open("four.txt", "r")
allMessages = []
for item in fourList:
    key, message, maxScore = Challenge13.singleByteXOR(item.strip())
    current = {'key': key, 'message': message, 'maxScore': maxScore}
    allMessages.append(current)

topMessage = sorted(allMessages, key = lambda item: item['maxScore'], reverse=True)[0]
print(topMessage['message'])
    
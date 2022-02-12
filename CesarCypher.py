"""





msg = str(input("Digite uma mensagem > "))



aux = list(msg)

print(aux)


msgCifrada = []

for i in aux:
    msgCifrada.append(chr(ord(i) + 3))


novaString = ''.join(msgCifrada)


print(f"Mensagem cifrada: {novaString}")



"""


def cypher(msg):
    newMsg = []
    for i in msg:
        newMsg.append(chr(ord(i) + 3))


    return ''.join(newMsg)



def decodeMsg(msg):
    newMsg = []
    for i in msg:
        newMsg.append(chr(ord(i) - 3))


    return ''.join(newMsg)


print(cypher('eu te amo muito'))
print(decodeMsg('rod'))







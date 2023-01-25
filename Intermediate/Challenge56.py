file = open("56EncryptedMessage.txt")
sentence=""
shift=0
line = file.readline()
shift = int(line)
line = file.readline()
sentence=line
    
sent = ""

for char in sentence:
    if char == " ":
        sent += " "
    else: 
        s = (ord(char) - 97) - shift
        if (s <= 0):
            s += 26
        s += 97
        sent += chr(s)
        
print(sent)

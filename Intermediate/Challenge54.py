file = open("CorruptedFile.txt", "r")
sentence = ""
line = file.readline()
for x in range(0,len(line),2):
    sentence += line[x]
    
file.close()

print(sentence)

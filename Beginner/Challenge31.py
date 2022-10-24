s = input("What is your sentence?")
sentence = list(s)
new = ""
hi = len(sentence)
#while (i>0):
    #i-=1
for i in sentence:
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        pass
    else:
        new += i
#s=sentence.join()
print(new)

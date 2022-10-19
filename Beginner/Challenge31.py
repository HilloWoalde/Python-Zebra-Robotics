s = input("What is your sentence?")
sentence = list(s)
vow=0
i = len(sentence)
while (i>0):
    i-=1
    vow=sentence[i]
    if (vow == "a" or vow == "e" or vow == "i" or vow == "o" or vow == "u"):
        print(sentence[i])
        sentence.pop(i)
s=sentence.join()

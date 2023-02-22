sentence=input('input sentence pls')
words=sentence.split()
odd=open("55oddlines.txt", "w")
even=open("55evenlines.txt", "w")
for i in range(0, len(words)):
    if i%2 == 0:
        even.write(words[i]+"\n")
    else:
        odd.write(words[i]+"\n")
odd.close()
even.close()

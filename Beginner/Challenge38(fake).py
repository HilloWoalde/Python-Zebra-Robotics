#while True:
    #print(ord(input("please enter one character to convert to code")))
    #print(chr(int(input("please enter one character code"))))
lis = []
phrase = ""
ed = input("Do you want to encrypt or decrypt?")
fcode = 0
final = ""
movement = 1
mid = []
index = 0
lis2 = []
if (ed == "encrypt"):
    phrase = input("What do you want to encrypt?")
    lis = list(phrase)
    lis2 = lis
    movement = int(input("What is your movement speed"))
    mid = lis
    for x in range(0, movement):
        if x == movement-1:
            for i in mid:
                if (i != " " and i != "z"):
                    fcode = ord(i)+1
                    final += chr(fcode)
                elif (i == "z"):
                    final += "a"
                elif (i == " "):
                    final += " "
        else:
            for i in mid:
                if (i != " " and i != "z"):
                    fcode = ord(i)+1
                    index = lis2.index(i)
                    lis2.pop(index)
                    lis2.insert(index, "*")
                    mid.pop(index)
                    mid.insert(index, chr(fcode))
                elif (i == "z"):
                    fcode = ord(i)+1
                    index = lis2.index(i)
                    lis2.pop(index)
                    lis2.insert(index, "*")
                    mid.pop(index)
                    mid.insert(index, "a")
                elif (i == " "):
                    fcode = ord(i)+1
                    index = lis2.index(i)
                    lis2.pop(index)
                    lis2.insert(index, "*")
                    mid.pop(index)
                    mid.insert(index, " ")
    print(final)
elif (ed == "decrypt"):
    phrase = input("What do you want to decrypt?")
    lis = list(phrase)
    movement = int(input("What is your movement speed"))
    for x in range(0, movement):
        for i in lis:
            if (i != " " and i != "a"):
                fcode = ord(i)-1
                final += chr(fcode)
            elif (i == "a"):
                final += "z"
            elif (i == " "):
                final += " "
        phrase
            
    print(phrase)
else:
    print("Please answer in only lowercase and type 'encrypt' or 'decrypt' (without the 's)")

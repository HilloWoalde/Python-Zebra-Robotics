#while True:
    #print(ord(input("please enter one character to convert to code")))
    #print(chr(int(input("please enter one character code"))))
lis = []
phrase = ""
ed = input("Do you want to encrypt or decrypt?")
fcode = 0
final = ""
if (ed == "encrypt"):
    phrase = input("What do you want to encrypt?")
    lis = list(phrase)
    for i in lis:
        if (i != " " and i != "z"):
            fcode = ord(i)+1
            final += chr(fcode)
        elif (i == "z"):
            final += "a"
        elif (i == " "):
            final += " "
    print(final)
elif (ed == "decrypt"):
    phrase = input("What do you want to decrypt?")
    lis = list(phrase)
    for i in lis:
        if (i != " " and i != "a"):
            fcode = ord(i)-1
            final += chr(fcode)
        elif (i == "a"):
            final += "z"
        elif (i == " "):
            final += " "
    print(final)
else:
    print("Please answer in only lowercase and type 'encrypt' or 'decrypt' (without the 's)")

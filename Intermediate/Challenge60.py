sentence = input("Enter a sentence(lowercase letters only): ")
shift = int(input("How much should the shift be? Enter: "))
sent = ""

for char in sentence:
    if char == " ":
        sent += " "
    else: 
        s = (ord(char)) + shift
        if (s >= 123):
            s -= 26
        sent += chr(s)
file=open("60ceaserencryption.txt", "w")
file.write(sent)
file.close()

sentence = input("Enter a sentence(lowercase letters only): ")
shift = int(input("How much should the shift be? Enter: "))
sent = ""

for char in sentence:
    if char == " ":
        sent += " "
    else: 
        s = (ord(char) - 97) + shift
        if (s >= 26):
            s -= 26
        s += 97
        sent += chr(s)
        
print(sent)

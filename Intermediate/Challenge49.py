hi = []
def stringToList(string, rev = "False"):
    new = []
    reverse = bool(rev)
    for i in string:
        new.append(i)
    if reverse == True:
        new.reverse()
    return(new)
hi = stringToList(input("What is a lsit"), input("Reverse?"))
print(hi)

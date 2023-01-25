def stringToList(string):
    new = []
    for i in string:
        new.append(i)
    return(new)
def listToString(lis):
    new = ""
    for i in lis:
        new += (i)
    return(new)
print(stringToList(input("What is a lsit")))
#print(listToString(stringToList(input("What is a lsit"))))

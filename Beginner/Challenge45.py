def showstars(rows):
    stri = "*"
    for i in range(1, rows+1):
        print(stri*i)
while True:
    showstars(int(input("How many rows?")))


#while True:
#    for i in range(0, int(input("How many rows?"))):
#        print("*"*i)
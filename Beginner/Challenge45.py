def showstars(rows):
    lis = []
    for i in range(0, rows):
        lis.append("*")
        print(str(lis))
while True:
    showstars(int(input("How many rows?")))

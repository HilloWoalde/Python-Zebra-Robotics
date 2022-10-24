var = input("What do you want to calculate the sum of all numbers between it and one?")
flo = int(var)+1
sui = 0
#while (flo > 0):
    #sui += flo
    #flo -= 1
    #print(flo)
    #print(sui)
for i in range(0,flo,1):
    sui += i
print(sui)

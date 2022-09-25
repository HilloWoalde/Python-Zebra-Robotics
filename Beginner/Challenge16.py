i1 = int(input("Price of item 1: "))
i2 = int(input("Price of item 2: "))
i3 = int(input("Price of item 3: "))
subtotal = i1+i2+i3
tax = 0.15
total = subtotal*(1+tax)
print("Your total is " + str(total)) #+ " with your subtotal being " + str(subtotal) + "and tax being " + str(tax) ".")
#print("test")

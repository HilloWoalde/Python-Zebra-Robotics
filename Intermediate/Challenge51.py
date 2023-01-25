tipVal = 0
glomoney = 1000 #int(input("How much money did you spend?"))
glopercent = 27 #int(input("How much of a tip would you like to give? (leave blank for reg 15%)"))
def tipCalc(money, percent=15):
    global tipVal
    tipVal = money*(percent/100)
tipCalc(glomoney, glopercent)
print(tipVal)
glomoney = 1000
glopercent = 16
tipCalc(glomoney, glopercent)
print(tipVal)
glomoney = 1000
tipCalc(glomoney)
print(tipVal)
tipCalc(glomoney)
print(tipVal)

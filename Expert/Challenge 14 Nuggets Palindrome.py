ded = []
def NUGGET(n):
    if n == 0:
        return True
    elif n < 4 or n in ded:
        if n not in ded:
            ded.append(n)
        return False
    else:
        if n>=50:
            if NUGGET(n - 50):
                return True
            elif NUGGET(n - 10):
                return True
            elif NUGGET(n - 6):
                return True
            elif NUGGET(n - 4):
                return True
        if n>=10:
            if NUGGET(n - 10):
                return True
            elif NUGGET(n - 6):
                return True
            elif NUGGET(n - 4):
                return True
        elif n>=6:
            if NUGGET(n - 6):
                return True
            elif NUGGET(n - 4):
                return True
        elif NUGGET(n - 4):
            return True
        if n-6 not in ded:
            ded.append(n-6)
        if n-4 not in ded:
            ded.append(n-4)
        if n not in ded:
            ded.append(n)

nuggets = int(input("NUGGET"))
if NUGGET(nuggets):
    print(ded)
    print("You can buy " + str(nuggets) + " chicken nuggets.")
else:
    print(ded)
    print("You cannot buy " + str(nuggets) + " chicken nuggets with the available pack sizes.")

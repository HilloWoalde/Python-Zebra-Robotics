#def findFactors(x, y):
#    factors=[]
#    if x>y:
#        z=x
#    else:
#        z=y
#    for i in range (1,z): 
#        if x%i==0 and y%i==0:
#            factors.append(i)
#    return(factors)
primeFactors=[]


def findBigger(x, y):
    if x>y:
        z=x
    else:
        z=y
    return(z)

def findFactors(x, y):
    helper(x, y, findBigger(x,y))
    factors = []
    primeFactors.append(1)
    for i in primeFactors:
        primeFactors.remove(i)
        for x in primeFactors:
            if ((i*x) in factors) == False:
                factors.append(i*x)
    factors.sort()
    return(factors)

def helper(x, y, z):
    if x == 1 or y == 1:
        return(primeFactors)
    for i in range(2,z):
        if x%i==0 and y%i==0:
            primeFactors.append(i)
            helper(int(x/i), int(y/i), findBigger(int(x/i),int(y/i)))
            break
#4, 12




print(findFactors(int(input("Whaz 1st num")), int(input("Whaz 2nd num"))))
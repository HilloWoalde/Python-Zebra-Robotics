def findFactors(x, y):
    factors=[]
    if x>y:z=x
    else:z=y
    for i in range (1,z): 
        if x%i==0 and y%i==0:factors.append(i)
    return(factors)
print(findFactors(int(input("Whaz 1st num")), int(input("Whaz 2nd num"))))
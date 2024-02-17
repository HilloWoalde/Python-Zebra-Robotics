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
def findFactors(num1, num2, currentFactor=1):
    commonFactors = []

    if currentFactor > min(num1, num2):
        return commonFactors

    if num1 % currentFactor == 0 and num2 % currentFactor == 0:
        commonFactors.append(currentFactor)

    commonFactors += findFactors(num1, num2, currentFactor + 1)

    return commonFactors

result = findFactors(4, 12)
print(result)


print(findFactors(int(input("Whaz 1st num")), int(input("Whaz 2nd num"))))
'''
def twoSum(nums, target):
    visited_numbers = {}
    for i in nums:
        otherNum = target - i
        if visited_numbers.get(i):  
            return True  
        else:
            visited_numbers[otherNum] = i
    return False
coins_str = input("")
coins = [int(digit) for digit in coins_str.strip('[], \r, \n, [, ]').split(', ')]
coins.append(0)
print(coins)
big=0
all = True
for i in coins:
    big+=i
print(big)
for i in range(1, big):
    print(i)
    print(twoSum(coins, i))
    if twoSum(coins, i) == False:
        print(i)
        all=False
        break
if all == True:
    print(big+1)
'''
#def twoSum(nums, target):
#    visited_numbers = {}
#    for i in nums:
#        otherNum = target - i  
#        if otherNum in visited_numbers:  
#            return [i, otherNum]  
#        else:
#            visited_numbers[i] = i
#print(twoSum([3,2,4,1,9], 12))

def twoSum(nums, target):
    visited_numbers = {}
    for i in nums:
        otherNum = target - i
        if visited_numbers.get(i):  
            return [i, otherNum]  
        else:
            visited_numbers[otherNum] = i
print(twoSum([13,20,47,1,9], 10))
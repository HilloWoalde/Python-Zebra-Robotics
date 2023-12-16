def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    result = [candy + extraCandies >= max_candies for candy in candies]
    return result

cand = input("")
extra_candies = int(input(""))
candies = [int(digit) for digit in cand.strip('[],\r,\n,[,], ').split(', ')]

result_array = kidsWithCandies(candies, extra_candies)
print(result_array)
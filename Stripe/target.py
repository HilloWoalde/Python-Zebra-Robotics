def two_sum(nums, target):
    # Create a dictionary to store the complement of each element
    complement_dict = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Check if the complement exists in the dictionary
        complement = target - num
        if complement in complement_dict:
            # Return the indices of the two numbers that add up to the target
            return [complement_dict[complement], i]
        
        # Update the dictionary with the current element and its index
        complement_dict[num] = i

    # If no solution is found, return an empty list or handle it as needed
    return []

nums = input("")
target = int(input(""))
num_list = [int(digit) for digit in nums.strip('[], \r, \n').split(', ')]
result = two_sum(num_list, target)
print(result)
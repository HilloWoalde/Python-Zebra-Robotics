def addToArrayForm(num_str, k):
    # Convert num_str to a list of its digits
    num_list = [int(digit) for digit in num_str.strip('[], \r, \n').split(', ')]
    
    # Initialize variables for carry and index
    carry = 0
    index = len(num_list) - 1
    
    # Iterate through the digits of num_list and add k
    while k > 0 or carry:
        # Get the current digit of num_list and add k and carry
        digit_sum = num_list[index] + k % 10 + carry
        
        # Update the digit and carry values
        num_list[index] = digit_sum % 10
        carry = digit_sum // 10
        
        # Move to the next digit
        index -= 1
        k //= 10

        # If we reach the beginning of num_list and there's still carry, add a new digit
        if index < 0 and carry:
            num_list.insert(0, carry)
            break

    return num_list

# Example usage
num_str = input("")
k = int(input(""))
result = addToArrayForm(num_str, k)
print(result)
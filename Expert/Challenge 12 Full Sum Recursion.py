def sum_numbers_recursive(x):
    # Base case: if x is 1, return 1
    if x == 1:
        return 1
    # Recursive case: add x to the sum of numbers from 1 to x-1
    else:
        return x + sum_numbers_recursive(x-1)

# Get input from the user
user_input = int(input("Enter an integer (X): "))

# Call the recursive function and print the result
result = sum_numbers_recursive(user_input)
print("The sum of numbers from 1 to " + str(user_input) + " is: " + str(result))
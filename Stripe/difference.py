def difference_between_largest_and_smallest(num):
    digits = list(str(num))

    largest_num = int(''.join(sorted(digits, reverse=True)))
    smallest_num = int(''.join(sorted(digits,)))

    difference = largest_num - smallest_num

    return difference

number = int(input(""))
result = difference_between_largest_and_smallest(number)
print(result)
import random

credit_card_number = ""

def make_random_number(number_of_element):
    random_numbers = []
    for i in range(number_of_element):
        random_numbers.append(random.randint(0, 9))
    return random_numbers

def luhn_algorithm():
    random_master_int = make_random_number(13)
    random_master_int.insert(0,5)
    random_master_int.insert(1,4)
    sum_even = []
    sum_odd = []
    for index,element in enumerate(random_master_int):
        if index % 2 != 0:
            r = random_master_int[index] * 2
            character_string = list(str(r))
            character_int = map(int, character_string)
            sum_even.append(sum(character_int))
        if index % 2 == 0:
            sum_odd.append(element)
    total_sum = sum(sum_even)+sum(sum_odd) * 9
    random_master_int.append(total_sum % 10)
    credit_card_number = ''.join(map(str, random_master_int))
    return(credit_card_number)

print(luhn_algorithm())
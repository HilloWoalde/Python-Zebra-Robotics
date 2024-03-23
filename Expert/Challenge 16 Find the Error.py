def quicksort(lst: list) -> list:
    if len(lst) < 2:
        return lst[:]
    else:
        pivot = lst[0]
        smaller, bigger = _partition(lst[1:], pivot)
        smaller_sorted = quicksort(smaller)
        bigger_sorted = quicksort(bigger)
        return smaller_sorted + [pivot] + bigger_sorted

def _partition(lst: list, pivot: any) -> tuple[list, list, list]:
    smaller = []
    bigger = []
    for item in lst:
        if item <= pivot: 
            smaller.append(item)
        else:
            bigger.append(item)

    return(smaller, bigger)

print(quicksort([10000000, 4235, 4235, 4235, 9457, 3245,3567, 45, 658, 235, 3657,4235, 479992, 57,46]))
print(quicksort([123, 45.6, -78, 9.0]))

[45, 132, 92]
pivot = 45
smaller = [45]
bigger = [132, 92]
biggerpivot = 132
biggersmaller = [132, 92]
biggerbigger = []
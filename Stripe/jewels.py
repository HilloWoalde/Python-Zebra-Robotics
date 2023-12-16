def numJewelsInStones(jewels, stones):
    # Use a set for faster lookup
    jewel_set = set(jewels)

    # Count the number of stones that are also jewels
    count = 0
    for stone in stones:
        if stone in jewel_set:
            count += 1

    return count

# Example usage
jewels = input("")
stones = input("")
result = numJewelsInStones(jewels, stones)
print(result)

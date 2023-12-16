def permuteVowels(s):
    vowels = "aeiouAEIOU"
    vowel_positions = [i for i, char in enumerate(s) if char in vowels]
    sorted_vowels = sorted([s[i] for i in vowel_positions])

    result = list(s)
    for i, vowel_pos in enumerate(vowel_positions):
        result[vowel_pos] = sorted_vowels[i]

    return "".join(result)

# usage
s = input("")
result = permuteVowels(s)
print(result)
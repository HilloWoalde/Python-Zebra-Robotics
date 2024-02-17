def is_palindrome(word):
    if len(word) <= 1:
        return True
    
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False

word = input("What word would you like to run 'is_palindrome' on?")
if is_palindrome(word):
    print(word+ " is a palindrome.")
else:
    print(word+ " is not a palindrome.")
def max (a, b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return a
print("This is an infinitly repeating algorithim to determine the maximum of two numbers")
while True:
    print(max(int(input("What is the first number?")),int(input("What is the second number?"))))

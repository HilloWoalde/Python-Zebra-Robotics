def worth(n):
    match(n):
        case "I":
            return 1
        case "V":
            return 5
        case "X":
            return 10
        case "L":
            return 50
        case "C":
            return 100
        case "D":
            return 500
        case "M":
            return 1000

def romanToDecimal(str):
    res = 0
    i = 0
    while (i < len(str)):
        s1 = worth(str[i])
        if (i + 1 < len(str)):
            s2 = worth(str[i + 1])
            if (s1 >= s2):
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res
print(romanToDecimal(input("")))
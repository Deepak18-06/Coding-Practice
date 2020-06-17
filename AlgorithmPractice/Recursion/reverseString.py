def RevS(s):
    print(s[len(s)])
    return s[len(s)]+s[:len(s)-1]

s = input()
RevS(s)
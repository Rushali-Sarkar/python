def repeatedString(s, n):
    
    while len(s) <= n:
        s = s + s

    s = s[0: n]

    return s.count('a')

print(repeatedString("abcac", 10))

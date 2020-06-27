def pangrams(s):
    alphabets = "abcdefghijklmnopqrstuvwzyz"
    s = s.lower()
    counter = sum([1 for letter in alphabets if letter in s])
    for letter in alphabets:
        print(letter)
        print(letter in s)
    if counter == 26:
        return "pangram"
    return "not pangram"

print(pangrams("We promptly judged antique ivory buckles for the prize"))

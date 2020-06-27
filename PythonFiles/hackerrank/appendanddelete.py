def main(string1: str, string2: str, o: int) -> int:

    length1 = len(string1)
    length2 = len(string2)
    length = min(length1, length2)

    operations = abs(length1 - length2)

    string1 = string1[0 : length]
    string2 = string2[0 : length]
    i = -1

    for index in range(length):

        if string1[index] != string2[index]:
            operations = operations + (len(string1[index: ]) * 2)
            i = index
            break

    if o < operations:
        return "No"

    if o == operations:
        return "Yes"
    print(string1)
    left = len(string1[0: index])
    if i == -1:
        left = len(string1)

    residual = o - operations

    print(left)
    print(residual)
    return operations



print(main("y", "yu", 2))
print(main("abcd", "abcdert", 10))


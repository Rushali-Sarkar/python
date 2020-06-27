def splitAndAddNumber(number: int) -> int:
    number = list(str(number))
    if len(number) == 1:
        return 1
    l = len(number) // 2
    first  = int("".join(number[:l]))
    second = int("".join(number[l:]))
    return sum([first, second])
def is_kaprekar(number: int) -> bool:
    x = number * number
    return number == splitAndAddNumber(x)
def kaprekarNumbers(p, q):
    p, q = int(p), int(q)
    x = []
    for number in range(p, q + 1):
        if is_kaprekar(number):
            x.append(number)
    print(*x)

kaprekarNumbers(1, 100000)

def nthrotate(arr: [int], n: int) -> [int]:
    return arr[-n: ] + arr[0: -n]


def circularArrayRotation(a, k, queries = 0):

    n = len(a) % k
    print(n)

    a = nthrotate(a, n)

    return a

print(circularArrayRotation([1, 2, 3], 2))
    
    

def triplets(arr: [int], d: int) -> int:
    length = len(arr)
    counter = 0
    for i in range(1, length - 1):
        print(arr[i + 1] - arr[i])
        print(arr[i] - arr[i - 1])
        if arr[i + 1] - arr[i] == arr[i] - arr[i - 1] == d:
            counter = counter + 1

    return counter 

print(triplets([1, 2, 4, 5, 7, 8, 10], 3))

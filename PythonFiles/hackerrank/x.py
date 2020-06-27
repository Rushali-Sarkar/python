def nonDivisibleSubset(k, arr):
    remainders = {remainder : [] for remainder in range(k)}
    for i in range(len(arr)):
        remainders[arr[i] % k].append(arr[i])
        count = 0
        if len(remainders[0]) > 0:
            count = 1
        S = set([(x, k-x) for x in range(1, k // 2 + 1)])
        for i, j in S:
            if i != j:
                if len(remainders[i]) > len(remainders[j]):
                    count += len(remainders[i])
                else:
                    count += len(remainders[j])
            else:
                if len(remainders[i]) > 0:
                    count += 1
    return count

import itertools


def findsubsets(sets: [int], partition: int) -> [int]:
    return list(itertools.combinations(sets, partition))


def divisibleSumPairs(sets: [int], divisor: int) -> int:
    combinations = findsubsets(sets, 2)
    return sum([1 for subset in combinations if (sum(subset) % divisor) == 0])


sets = [1, 3, 2, 6, 1, 2]
divisor = 3
print(divisibleSumPairs(sets, divisor))

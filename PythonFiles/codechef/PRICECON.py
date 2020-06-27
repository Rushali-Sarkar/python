def losses(cost: [int], priceCeiling: int) -> int:

    loss = 0 

    for money in cost:

        if money > priceCeiling:
            loss = loss + (money - priceCeiling)

    return loss


testcases = int(input())

for i in range(testcases):

    n, maxprice = input().split(" ")
    n, maxprice = int(n), int(maxprice)
    cost = list(map(int, input().split()))

    print(losses(cost, maxprice))






"""print(losses([10, 2, 3, 4, 5], 4))
print(losses([1, 2, 3, 4, 5, 6, 7], 15))
print(losses([10, 9, 8, 7, 6], 5))"""

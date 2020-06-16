def bonAppetit(bill: [int], discard: int, shared: int) -> str:
    discardedItem = bill[discard]
    bill.remove(discardedItem)
    annasShare = sum(bill) // 2
    diff = shared - annasShare
    if diff == 0:
        return "Bon Appetit"
    return str(diff)

print(bonAppetit([3, 10, 2, 9], 1, 7))



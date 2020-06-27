def main(people: [int]) -> str:
    change5  = 0
    change10 = 0
    change15 = 0
    for money in people:
        if money == 5:
            change5 = change5 + 5
        elif money == 10 and change5 >= 5:
            change5 = change5 - 5
            change10 = change10 + 10                                                        
        elif money == 15:
            if change10 >= 10:
                change10 = change10 - 10
                change15 = change15 + 1             
            elif change5 >= 10:
                change5 = change5 - 10
                change15 = change15 + 15
            else:
                return "NO"
        else:
            return "NO"
    return "YES"

print(main([5, 10]))
print(main([10, 5]))
print(main([5, 15]))



def subtract(sticks: [int], tosubtract: int) -> [int]:
    return [(element - tosubtract) for element in sticks if (element - tosubtract) != 0]

def cut(sticks: [int]) -> [int]:
    lengths = []
    while len(sticks) != 0 :
        lengths.append(len(sticks))
        tosubtract = min(sticks)
        sticks = subtract(sticks, tosubtract)
    return lengths

print(cut([5, 4, 4, 2, 2, 8]))
print(cut([1, 2, 3, 4, 3, 3, 2, 1]))


         

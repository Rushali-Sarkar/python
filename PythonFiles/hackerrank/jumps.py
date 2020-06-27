"0, 0, 1, 0, 0, 1, 0"

THUNDER = 1
CUMULUS = 0

def jumpingOnClouds(clouds: [int]) -> int:

    index = 0
    jumps = []

    while index < len(clouds) - 2:

        if clouds[index + 2] == CUMULUS:
            jumps.append(index + 2)
            index  = index + 2

        elif clouds[index + 1] == CUMULUS:
            jumps.append(index + 1)
            index = index + 1

    
    return jumps

clouds = [0, 0, 0, 1, 0, 0]
jumps = jumpingOnClouds(clouds)
print(jumps)

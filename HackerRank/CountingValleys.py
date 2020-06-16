# A mountain is a sequence of consecutive steps above sea level.
# A mountain starts with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level.
# A valley starts with a step down from sea level and ending with a step up to sea level.

UPHILL   = "U"
DOWNHILL = "D"

def countingValleys(steps: int, path: str) -> int:

    start = 0
    valley = 0
    below = False

    for move in path:

        if move == UPHILL:
            start = start + 1

        if move == DOWNHILL:
            start = start - 1

        if start < 0:
            below = True

        if start == 0 and below:
            valley = valley + 1
            below = False

    return valley

print(countingValleys(8, "UDDDUDUU"))
print(countingValleys(10, "UDUUUDUDDD"))
print(countingValleys(10, "DUDDDUUDUU"))


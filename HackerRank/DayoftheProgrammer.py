def isLeapGregorian(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def isLeapJulian(year: int) -> bool:
    return (year - 1700) % 4 == 0

def dayOfProgrammer(year: int) -> str:
    
    if year == 1918:
        return "26.09.1918"

    if year >= 1919:
        if isLeapGregorian(year):
            return "12.09." + str(year)
        return "13.09." + str(year)

    if isLeapJulian(year):
        return "12.09." + str(year)
    return "13.09." + str(year)


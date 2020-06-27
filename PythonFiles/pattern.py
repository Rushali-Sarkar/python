PLUS,      EQUAL,      DASH,         VERTICAL, SPACE = "+", "=", "-", "|", " "
LEFT_ANGULAR, RIGHT_ANGULAR   = "<", ">"

def endLines(size: int) -> [str]:
    return [PLUS + DASH * size * 2 + PLUS]

def middleLine(size: int) -> [str]:
    return  [VERTICAL + LEFT_ANGULAR + DASH * (size * 2 - 2) + RIGHT_ANGULAR + VERTICAL]\
            if size % 2 == 0 else\
            [VERTICAL + LEFT_ANGULAR + EQUAL * (size * 2 - 2) + RIGHT_ANGULAR + VERTICAL] 

def triangle(size: int, Type = 1) -> [str]:
    BACKSLASH, FRONTSLASH = "\ ".strip(), "/"
    if Type == -1:
        BACKSLASH, FRONTSLASH = FRONTSLASH, BACKSLASH
    return [[VERTICAL + SPACE * (size - i) + FRONTSLASH + DASH  * (i * 2 - 2) + BACKSLASH + SPACE * (size - i) + VERTICAL]\
            if i % 2 == 0 else\
            [VERTICAL + SPACE * (size - i) + FRONTSLASH + EQUAL * (i * 2 - 2) + BACKSLASH + SPACE * (size - i) + VERTICAL]\
            for i in range(1, size)][::Type]

def pattern(size: int) -> [str]:
    return [endLines(size)] +\
           [line for line in triangle(size)] +\
           [middleLine(size)] +\
           [line for line in triangle(size, -1)] +\
           [endLines(size)]

size = int(input())
diamondPattern = pattern(size)
for line in diamondPattern:
    print(*line)

def maxpairs(students: str) -> int:
    
    girl = 'x'
    boy = 'y'
    pair = 0
    index = 0

    while(index < len(students) - 1):

        if (students[index] == girl and students[index + 1] == boy) or (students[index] == boy and students[index + 1] == girl):
            pair = pair + 1
            index = index + 1

        index = index + 1

    return pair

print(maxpairs("xy"))
print(maxpairs("xyxxy"))
print(maxpairs("yy"))


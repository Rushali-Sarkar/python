KNOWN = "1"

def assignSubjects(topics: [str]) -> [int]:
        return [[index + 1 for index, topic in enumerate(people) if topic == KNOWN] for people in topics]

def findmax(knowntopics: [int]) -> (int, int):
    maximum = []

    for index, each in enumerate(knowntopics):
        for element in knowntopics[index + 1:]:
            together = list(set(each + element))
            maximum.append(len(together))

    maximum = sorted(maximum)
    return maximum[-1], maximum.count(maximum[-1])

assigned = assignSubjects(["10101", "11100", "11010", "00101"])
find = findmax(assigned)
print(find)


            
        

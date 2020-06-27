s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
k = 7
s = [element % 7 for element in s]
s.sort()
for each in s:

    if each and k - each in s:
        if s.count(each) > s.count(k - each):
            s.remove(k - each)
        else:
            s.remove(each)

print(s)



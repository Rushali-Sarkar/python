import sys

nameandroll = open("../TextFiles/student.txt", "w+")
names = sys.argv[1:]
print(names)
for name in names:
    nameandroll.write(name)
nameandroll = nameandroll.readlines()
for line in nameandroll:
    print(line)




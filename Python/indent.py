#!/usr/bin/python3

x = 42
y = 73

if x < y:
        z = 112
        print("x < y: x is {} and y is {}".format(x, y))
        print("line 2")
        print("line 3")
elif x > y:
        print("x > y: x is {} and y is {}".format(x, y))
elif x == y:
        print("x == y: x is {} and y is {}".format(x, y))
else:
        print("do something else")

print("line 4")
print("something else")
print("z is {}".format(z))

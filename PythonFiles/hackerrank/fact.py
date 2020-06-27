def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)

    return fact

print(factorial(45))


#!/usr/bin/python3

import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def gcd(number1: int, number2: int) ->  int:
    if number1 == 0:
        return number2
    return gcd(number2 % number1, number1)


def eulertotient(number: int) -> int:
    return len([n for n in range(1, number) if gcd(n, number) == 1])

def eulergraph(number: int) -> {int: int}:
    return {n : eulertotient(n) for n in range(2, number)}

graph = eulergraph(1000)
for x, y in graph.items():
    plt.scatter(x, y, c = "black")

plt.show()

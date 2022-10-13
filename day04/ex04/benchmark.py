#!/bin/python3
import timeit
import sys
import random
from collections import Counter


def my_create_dict(lst: list[int]):
    dct = {}
    for i in lst:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct


def my_top(lst):
    dct = my_create_dict(lst)
    dct = sorted(dct.items(), key=(lambda x: x[1]), reverse=True)[:10]
    dct = dict(dct)
    return dct


def counter_create_dict(lst):
    c = Counter(lst)
    return c


def counter_top(lst):
    c = counter_create_dict(lst)
    return c.most_common(10)


def run():
    lst = [random.randint(0, 100) for x in range(1_000_000)]
    number = 1
    time = timeit.Timer(lambda: my_create_dict(lst)).timeit(number=number)
    print(f"my function: {time:.8f}")
    time = timeit.Timer(lambda: counter_create_dict(lst)).timeit(number=number)
    print(f"Counter: {time:.8f}")
    time = timeit.Timer(lambda: my_top(lst)).timeit(number=number)
    print(f"my top: {time:.8f}")
    time = timeit.Timer(lambda: counter_top(lst)).timeit(number=number)
    print(f"Counter's top: {time:.8f}")



if __name__ == "__main__":
    run()

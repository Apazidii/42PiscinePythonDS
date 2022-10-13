#!/bin/python3
import timeit
import sys
from functools import reduce


def loop_sum(k):
    res = 0
    for i in k:
        res += i*i
    return res


def reduce_sum(k):
    res = reduce(lambda x, y: x + y*y, k)
    return res


def run(type_f, number, k):
    my_range = range(1, k + 1)
    if type_f == "loop":
        time = timeit.Timer(lambda: loop_sum(my_range)).timeit(number=number)
    elif type_f == "reduce":
        time = timeit.Timer(lambda: reduce_sum(my_range)).timeit(number=number)
    else:
        raise Exception("Wrong name of the func")
    print(time)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        run(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    else:
        raise Exception("Invalid number of argument")

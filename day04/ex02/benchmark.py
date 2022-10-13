#!/bin/python3
import timeit
import sys


def loop_check(email: list[str]):
    res = []
    for i in email:
        if i.endswith("@gmail.com"):
            res.append(i)
    return res


def list_check(email: list[str]):
    res = [i for i in email if i.endswith("@gmail.com")]
    return res


def map_check(email: list[str]):
    res = (map(lambda x: x if x.endswith("@gmail.com") else None, email))
    return list(res)


def filter_check(email: list[str]):
    res = filter(lambda x: x.endswith("@gmail.com"), email)
    return list(res)


def run(type, number):

    emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5

    if type == "loop":
        time = timeit.Timer(lambda:   loop_check(emails)).timeit(number=number)
    elif type == "list comprehension":
        time = timeit.Timer(lambda:   list_check(emails)).timeit(number=number)
    elif type == "map":
        time = timeit.Timer(lambda:    map_check(emails)).timeit(number=number)
    elif type == "filter":
        time = timeit.Timer(lambda: filter_check(emails)).timeit(number=number)
    else:
        raise Exception("Wrong name of the func")
    print(time)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        run(sys.argv[1], int(sys.argv[2]))
    else:
        raise Exception("Invalid number of argument")

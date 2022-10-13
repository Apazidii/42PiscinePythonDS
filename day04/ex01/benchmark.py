#!/bin/python3
import timeit


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
    return res

def run():
    number = 90_000

    emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5

    loop_time = timeit.Timer(lambda: loop_check(emails)).timeit(number=number)
    list_time = timeit.Timer(lambda: list_check(emails)).timeit(number=number)
    map_time  = timeit.Timer(lambda:  map_check(emails)).timeit(number=number)

    times = sorted([loop_time, list_time, map_time])
    if times[0] == loop_time:
        print("it is better to use a loop")
    elif times[0] == list_time:
        print("it is better to use a list comprehension")
    elif times[0] == map_time:
        print("it is better to use a map")
    print(f"{times[0]} vs {times[1]} vs {times[2]}")


if __name__ == "__main__":
    run()

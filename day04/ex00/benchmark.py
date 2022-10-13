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


def run():
    number = 90_000

    emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5

    loop_time = timeit.Timer(lambda: loop_check(emails)).timeit(number=number)
    list_time = timeit.Timer(lambda: list_check(emails)).timeit(number=number)

    if loop_time < list_time:
        print("it is better to use a loop")
    else:
        print("it is better to use a list comprehension")
    print(f"{min(loop_time, list_time)} vs {max(loop_time, list_time)}")

if __name__ == "__main__":
    run()

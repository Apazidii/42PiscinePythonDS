import logging
from random import randint

class Research:
    def __init__(self, file):
        self.file = file

    def file_reader(self, has_header=True):
        logging.info(f"read file {self.file}")
        with open(self.file, "r") as f:
            res = []
            arr = f.read().split('\n')
            if has_header:
                if len(arr[0].split(',')) != 2:
                    raise Exception("Invalid header in csv")
                arr = arr[1:]
            for i in arr:
                if i != "0,1" and i != "1,0":
                    raise Exception("Invalid data in csv")
                else:
                    res.append(list(eval(i)))
            return res

    class Calculations:

        def __init__(self, lst):
            self.lst = lst

        def counts(self):
            logging.info("calculate counts")
            a = 0
            b = 0
            for i in self.lst:
                if i[0] == 0:
                    a += 1
                else:
                    b += 1
            return a, b

        def fractions(self):
            logging.info("calculate fractions")
            ln = len(self.lst)
            a, b = self.counts()
            return a / ln * 100, b / ln * 100


class Analytics(Research.Calculations):
    def predict_random(self, k):
        logging.info(f"generate random (step = {k})")
        pattern = [[0,1], [1, 0]]
        res = []
        for _ in range(0, k):
            res.append(pattern[randint(0, 1)].copy())
        return res

    def predict_last(self):
        logging.info("get last")
        return self.lst[-1]

    def save_file(self, data, file, exp):
        logging.info(f"save data to file {file}.{exp}")
        with open(f'{file}.{exp}', "w") as f:
            f.write(data)

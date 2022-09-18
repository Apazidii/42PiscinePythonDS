import sys


class Research:
    def __init__(self, file):

        self.file = file

    def file_reader(self, has_header=True):
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

        def counts(self, lst):
            a = 0
            b = 0
            for i in lst:
                if i[0] == 0:
                    a += 1
                else:
                    b += 1
            return a, b

        def fractions(self, lst):
            ln = len(lst)
            a, b = self.counts(lst)
            return a / ln * 100, b / ln * 100


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("invalid number arg")
    else:
        c = Research(sys.argv[1])
        data = c.file_reader()
        counts = c.Calculations().counts(data)
        fractions = c.Calculations().fractions(data)
        print(data)
        print(counts[0], counts[1])
        print(fractions[0], fractions[1])

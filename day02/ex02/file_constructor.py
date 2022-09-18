import sys

class Research:
    def __init__(self, file):

        self.file = file

    def file_reader(self):
        with open(self.file, "r") as f:
            res = f.read()
            arr = res.split('\n')
            if len(arr[0].split(',')) != 2:
                raise Exception("Invalid header in csv")
            arr = arr[1:]
            for i in arr:
                if i != "0,1" and i != "1,0":
                    raise Exception("Invalid data in csv")
            return res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("invalid number arg")
    else:
        c = Research(sys.argv[1])
        print(c.file_reader())

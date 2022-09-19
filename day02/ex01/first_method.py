class Research:
    def file_reader(self):
        with open("../ex05/data.csv", "r") as inp:
            return (inp.read())

if __name__ == "__main__":
    print(Research().file_reader())
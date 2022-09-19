import sys


def parser_email(s: str):
    return (s.split("@")[0].split("."))

def run(path):
    f = open(path, "r")
    s = f.read().split("\n")
    f.close()
    f = open("employees.tsv", "w")
    f.write("Name\tSurname\tE-mail\n")
    for i in s:
        t = parser_email(i)
        f.write(f"{t[0].title()}\t{t[1].title()}\t{i}\n")
    f.close()
if __name__ == "__main__":
    if len(sys.argv) == 2:
        run(sys.argv[1])
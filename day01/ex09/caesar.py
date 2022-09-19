import sys


def caesar(word: str, key: int):
    try:
        word.encode('ascii')
    except UnicodeEncodeError:
        raise Exception('The script does not support your language yet')

    base_lower = "abcdefghijklmnopqrstuvwxyz"
    base_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    res = ""
    for elem in word:
        if elem in base_upper:
            res += base_upper[(base_upper.index(elem) + key) % 26]
        elif elem in base_lower:
            res += base_lower[(base_lower.index(elem) + key) % 26]
        else:
            res += elem
    return res


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise Exception("Incorrect number of argument")
    else:
        if sys.argv[1] == "encode":
            print(caesar(sys.argv[2], int(sys.argv[3])))
        elif sys.argv[1] == "decode":
            print(caesar(sys.argv[2], -int(sys.argv[3])))
        else:
            raise Exception("Use encode or decode mode")

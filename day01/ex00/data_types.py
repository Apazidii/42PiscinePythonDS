def data_types():
    e1 = 42
    e2 = "forty two"
    e3 = 42.42
    e4 = True
    e5 = [4, 2]
    e6 = {4: 4, 2: 2}
    e7 = ("forty", "two")
    e8 = {"forty", "two"}

    arr = [e1, e2, e3, e4, e5, e6, e7, e8]

    for i, elem in enumerate(arr):
        arr[i] = str(type(elem).__name__)

    print(f'[{", ".join(arr)}]')

if __name__ == '__main__':
    data_types()




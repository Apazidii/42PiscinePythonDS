def list_to_dict():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]

    res = {}
    for elem in list_of_tuples:
        if elem[1] in res:
            res[int(elem[1])].append(elem[0])
        else:
            res[int(elem[1])] = [elem[0]]

    for i in sorted(res, reverse=True):
        for j in sorted(res[i]):
            print(j)


if __name__ == "__main__":
    list_to_dict()
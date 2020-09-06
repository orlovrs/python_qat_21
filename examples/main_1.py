def sum_int(a, b):
    return a + b


def sum_none(a, b):
    print(a + b)


if __name__ == '__main__':
    a = sum_int(1, 4)
    print(a)
    b = sum_none(1, 4)
    print(b)

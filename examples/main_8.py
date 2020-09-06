from examples.decorators import do_twice


@do_twice
def twice(s):
    print("Это вызов функции с аргументом {0}".format(s))


@do_twice
def with_many_args(s, t):
    print("{0} {1}".format(s, t))
    return "Done"


if __name__ == '__main__':
    print(with_many_args("Hello", "World"))

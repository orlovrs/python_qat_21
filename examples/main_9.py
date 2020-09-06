from examples.decorators import do_twice


@do_twice
def twice(s):
    print("{0}".format(s))
    return "Done"


if __name__ == '__main__':
    print(twice.__name__)

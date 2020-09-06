from examples.decorators import do_twice


@do_twice
def twice():
    print("Эта функция должна выполниться дважды")


if __name__ == '__main__':
    twice()

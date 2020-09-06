def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции")
        func()
        print("Конец выполнения функции")

    return wrapper


def my_first_decorator():
    print("Это мой первый декоратор!")


if __name__ == '__main__':
    my_first_decorator = my_decorator(my_first_decorator)
    my_first_decorator()
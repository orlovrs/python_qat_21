def parent(num):
    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    if num == 1:
        return first_child()
    else:
        return second_child()


if __name__ == '__main__':
    parent(0)

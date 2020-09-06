from datetime import datetime


def working_hours(func):
    def wrapper():
        if 0 <= datetime.now().hour < 6:
            func()
        else:
            pass  # Нерабочее время, выходим

    return wrapper


def writing_tests():
    print("Я пишу тесты на python!")


if __name__ == '__main__':
    writing_tests = working_hours(writing_tests)
    writing_tests()

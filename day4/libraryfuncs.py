x = 4

if x == 4:
    y = 7


def main():
    print('we are in main')


def myfunc(x):
    return x + 4


def xxx(p):
    if p < 4:
        y = 10

    print(y)


if __name__ == '__main__':
    print('Running the tests!')
    assert myfunc(8) == 12
else:
    print('I am', __name__)
    main()

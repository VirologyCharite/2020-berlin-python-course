#!/usr/bin/env python

import sys


def memoize(func):
    knownResults = {}

    def newfunc(*args):
        try:
            return knownResults[args]
        except KeyError:
            result = func(*args)
            # print(f'I am going to call the original function with {args}')
            knownResults[args] = result
            return result

    return newfunc


@memoize
def fib(n):
    f1, f2 = 0, 1
    if n == 0:
        return f1
    if n == 1:
        return f2
    return fib(n - 1) + fib(n - 2)


@memoize
def fact(n):
    if n == 1:
        return 1

    return fact(n - 1) * n


@memoize
def add(x, y):
    return x + y


if __name__ == '__main__':
    print(fib(int(sys.argv[1])))
    print(fact(int(sys.argv[1])))
    print(fact(2 * int(sys.argv[1])))
    print(add(int(sys.argv[1]), int(sys.argv[2])))

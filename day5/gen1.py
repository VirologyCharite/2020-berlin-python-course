#!/usr/bin/env python

import sys
from time import sleep


def squares(n):
    result = []

    for i in range(n):
        result.append(i * i)

    return result


def squares2(n):
    # print(f'Computing the first {n} squares.')
    for i in range(n):
        yield i * i
        # print('Continuing...')


results = squares2(int(sys.argv[1]))

# print('first:', next(results))
# print('second:', next(results))

for sq in results:
    print(sq)
    # sleep(2)

#!/usr/bin/env python

from itertools import chain, repeat

a = [1, 2, 3]
b = [4, 5, 6, 7]


# Our implementation of itertools.repeat
def myRepeat(value):
    while True:
        yield value


for i in chain(a, b, repeat(10)):
    print(i)


for i in zip(a, b):
    print(i)


def myEnumerate(things, start=0):
    index = start
    for thing in things:
        yield index, thing
        index += 1


animals = ('cat', 'dog', 'tiger', 'ant')

for index, animal in enumerate(animals, start=5):
    print(index, animal)

for index, animal in myEnumerate(animals, start=5):
    print(index, animal)

# index = 0
# for animal in animals:
#     index += 1
#     print(index - 1, animal)

#!/usr/bin/env python


class XX:
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b


x = XX()

print(x.add(4, 5))

print(XX.add(4, 5))

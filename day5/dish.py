#!/usr/bin/env python

import sys


def dinnerChecker(func):

    def newfunc(dish):
        # Do something to get ready.
        if dish == 'carrots':
            print('Oh, no, not carrots again! No!')
        else:
            func(dish)
            # Do something to clean up.
            print('Johannes, did you turn off the gas and close the fridge?')

    return newfunc


@dinnerChecker
def johannesMakeDinner(dish):
    print(f"Yes, Tali, I'll make you some {dish} right away!")




if __name__ == '__main__':
    # johannesMakeDinner = dinnerChecker(johannesMakeDinner)
    # saferDinnerFunc = dinnerChecker(johannesMakeDinner)
    # saferDinnerFunc(sys.argv[1])
    johannesMakeDinner(sys.argv[1])

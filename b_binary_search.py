#b_binary_search.py
'''
title: b_binary_search.py
author: kliment lo
date: 2023/09/07
'''

from random import randrange
from time import perf_counter
from statistics import mean



def createArray(SIZE):
    '''
    create an ordered array of approximate size SIZE
    :param SIZE: (int)
    :return: (list)
    '''
    numbers = []

    for i in range(2*SIZE):
        if randrange(2) == 1:
            numbers.append(i)
    return numbers

def binarySearch (LIST, VALUE):
    '''
    Search for a value within a list -recursive
    :param LIST: list(int)
    :param VALUE: (int)
    :return: (bool)
    '''

    MIDPOINT_INDEX = len(LIST)//2
    if LIST[MIDPOINT_INDEX] == VALUE: # base case
        return True
    else:
        # simplify the list and return the function
        if VALUE < LIST[MIDPOINT_INDEX]:
            return binarySearch(LIST[:MIDPOINT_INDEX], VALUE)
        else:
            return binarySearch(LIST[MIDPOINT_INDEX+1:], VALUE)

### MAIN PROGRAM CODE

if __name__ == "__main__":
    from myFunctions import *
    TIMES = []
    for i in range(30):
        NUMBERS = createArray(10000)
        NUMBER = NUMBERS[randrange(len(NUMBERS))] # chooses one of the randomly generated numbers
        START_TIME = perf_counter()
        FOUND = binarySearch(NUMBERS, NUMBER)
        END_TIME = perf_counter()

        TIMES.append(END_TIME - START_TIME)
        print(i+1)
    print(getAverage(TIMES))

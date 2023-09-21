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
    Search for a value within a list
    :param LIST: list(int)
    :param VALUE: (int)
    :return: (bool)
    '''

    start_index = 0
    end_index = len(LIST) - 1
    while start_index <= end_index:
        midpoint_index = (start_index + end_index) // 2
        if LIST[midpoint_index] == VALUE:
            return True
        elif VALUE > LIST[midpoint_index]:
            start_index = midpoint_index + 1
        else:
            end_index = midpoint_index
    return False


### MAIN PROGRAM CODE

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = createArray(10)
        NUMBER = NUMBERS[randrange(len(NUMBERS))] # chooses one of the randomly generated numbers
        START_TIME = perf_counter()
        FOUND = binarySearch(NUMBERS, NUMBER)
        END_TIME = perf_counter()

        print(f"""Number: {NUMBER}
Found: {FOUND}
""")
        TIMES.append(END_TIME - START_TIME)
    print(f"Mean: {mean(TIMES)}")
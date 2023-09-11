#c_bubble_sort.py

'''
title: c_bubble_sort.py
author: Kliment Lo
date: 2023/09/11
'''

from myFunctions import *

def bubbleSort(LIST):
    '''
    Compares adjacent values and moves the highest one to the end of the list.
    :param LIST: list (int)
    :return: (none) [lists persist inside and outside of a function]
    '''
    # [13, 8, 4, 21]
    for i in range(len(LIST)-1, 0, -1): # traverses backwards from the end to index 1
        for j in range(i): # traversing forward in the unsorted section of the list
            if LIST[j] > LIST[j+1]:# if left number is greater than the right number
                TEMP = LIST[j]
                LIST[j] = LIST[j+1]
                LIST[j+1] = TEMP
                # LIST[j], LIST[j+1] = LIST[j+1], LIST[j] (shorter abbreviated version that also works)

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        bubbleSort(NUMBERS)
        END_TIME = getTime()
        TIMES.append(END_TIME - START_TIME)
        print(i)
    print(getAverage(TIMES))


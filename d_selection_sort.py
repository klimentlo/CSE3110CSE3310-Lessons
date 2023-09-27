#d_selection_sort.py

'''
title: d_selection_sort.py
author: kliment-lo
date:2023/09/12
'''

from myFunctions import *

def selectionSort(LIST):
    '''
    select the lowest value in the unsorted part of the list and place it at the lowest index of the unsorted part of the list.
    :param LIST: list (int)
    :return: none
    '''

    for i in range(len(LIST)-1):
        MININUM_INDEX = i
        for j in range(i + 1, len(LIST)): # start from 1 above chosen value till the end of the list
            if LIST[j] < LIST[MININUM_INDEX]: # if next index is smaller than current lowest index
                MININUM_INDEX = j # make this new lowest index
        if LIST[MININUM_INDEX] < LIST[i]: # if lowest value is less than
            TEMP = LIST[i]
            LIST[i] = LIST[MININUM_INDEX]
            LIST[MININUM_INDEX] = TEMP

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        selectionSort(NUMBERS)
        END_TIME = getTime()
        TIMES.append(END_TIME - START_TIME)
        print(i)
    print(getAverage(TIMES))

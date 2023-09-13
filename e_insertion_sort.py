#e_insertion_sort.py

'''
title: e_insertion_sort.py
author: kliment_lo
date: 2023/09/13
'''

def insertionSort(LIST):
    '''
    takes the lowest index of the unsorted section and placed it in the sorted sectiom
    :param LIST: list(int)
    :return: (none)
    '''
    # [ 3, 5, 7, 4, 9]
    for i in range(1, len(LIST)):
        UNSORTED_VALUE = LIST[i] # 4
        HIGHEST_SORTED_INDEX = i - 1 # 7 (index 2)
        while HIGHEST_SORTED_INDEX >= 0 and UNSORTED_VALUE < LIST[HIGHEST_SORTED_INDEX]: #
            LIST[HIGHEST_SORTED_INDEX + 1 ] = LIST[HIGHEST_SORTED_INDEX] #
            HIGHEST_SORTED_INDEX = HIGHEST_SORTED_INDEX - 1 #
        LIST[HIGHEST_SORTED_INDEX + 1] = UNSORTED_VALUE



if __name__ == "__main__":
    from myFunctions import *

    TIMES = []

    for i in range(30):

        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        insertionSort(NUMBERS)
        END_TIME = getTime()
        TIMES.append(END_TIME - START_TIME)
        print(i)

    print(getAverage(TIMES))
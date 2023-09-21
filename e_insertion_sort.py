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
    LIST = [ 6, 8, 2, 0, 1, 4, 3, 7]
    # LIST = [ 6, 8, 2, 0, 1, 4, 3, 7]
    for i in range(1, len(LIST)): # starts from index one, to the end of the list (we skip the first number because( its considered "sorted" for now))
        UNSORTED_VALUE = LIST[i] #The program now saves the first unsorted value in the unsorted section [value: 8] i = 1
        HIGHEST_SORTED_INDEX = i - 1 # Everything before the unsorted_value is already "sorted" [ value: 0 ]
        while HIGHEST_SORTED_INDEX >= 0 and UNSORTED_VALUE < LIST[HIGHEST_SORTED_INDEX]: # when the highest sorted index is bigger than 0, and the unsorted value[8] is smaller than the largest sorted number[6]
            LIST[HIGHEST_SORTED_INDEX + 1 ] = LIST[HIGHEST_SORTED_INDEX] # replace
            HIGHEST_SORTED_INDEX = HIGHEST_SORTED_INDEX - 1 #
        LIST[HIGHEST_SORTED_INDEX + 1] = UNSORTED_VALUE # [place the unsorted value into its proper position
        print(i)



if __name__ == "__main__":
    from myFunctions import *

    TIMES = []
    NUMBERS = getRandomList(5)
    START_TIME = getTime()
    insertionSort(NUMBERS)
    END_TIME = getTime()
    TIMES.append(END_TIME - START_TIME)

    print(getAverage(TIMES))
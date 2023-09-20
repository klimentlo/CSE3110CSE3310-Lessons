#g_quick_sort.py

'''
title: quick sort example
author: kliment lo
date-created: 2023/09/18
'''

def quickSort(LIST, FIRST_INDEX, LAST_INDEX):
    '''
    assign the first value as the pivot and place it in its correct location
    :param LIST: list(int) -> unsorted
    :param FIRST_INDEX: (int)
    :param LAST_INDEX: (int)
    :return: none
    '''

    if FIRST_INDEX < LAST_INDEX: # test that the list is one or more
        PIVOT_VALUE = LIST[FIRST_INDEX]
        LEFT_INDEX = FIRST_INDEX + 1
        RIGHT_INDEX = LAST_INDEX

        DONE = False

        while not DONE: #iterative component
            while LEFT_INDEX <= RIGHT_INDEX and LIST[LEFT_INDEX] <= PIVOT_VALUE: #continues until finds value that is smaller than pivot and left index
                LEFT_INDEX += 1

            while RIGHT_INDEX >= LEFT_INDEX and LIST[RIGHT_INDEX] >= PIVOT_VALUE: # continues until
                RIGHT_INDEX -= 1

            if RIGHT_INDEX < LEFT_INDEX: # has the right index crossed over the left?
                DONE = True # exits while loop
            else:
                TEMP = LIST[LEFT_INDEX]
                LIST[LEFT_INDEX] = LIST[RIGHT_INDEX]
                LIST[RIGHT_INDEX] = TEMP

        TEMP = LIST[FIRST_INDEX]
        LIST[FIRST_INDEX] = LIST[RIGHT_INDEX]
        LIST[RIGHT_INDEX] = TEMP

        quickSort(LIST, FIRST_INDEX, RIGHT_INDEX - 1)
        quickSort(LIST, RIGHT_INDEX + 1, LAST_INDEX)

if __name__ == "__main__":
    from myFunctions import *

    TIMES = []
    for i in range(100):
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        quickSort(NUMBERS, 0, len(NUMBERS)-1)
        END_TIME = getTime()
        TIMES.append(END_TIME - START_TIME)
        print(i)
    print(getAverage(TIMES))
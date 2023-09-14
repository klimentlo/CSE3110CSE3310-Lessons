# f_merge_sort.py

'''
title: merge sort
author: kliment_lo
date_created: 2023/09/14
'''



def mergeSortedLists(LIST_LEFT, LIST_RIGHT):
    '''
    iterative merge of two sorted lists
    :param LIST_LEFT: list(int) -> sorted
    :param LIST_RIGHT: list(int) -> sorted
    :return: list(int) -> sorted
    '''

    # Special Case: where one or both lists are empty
    if len(LIST_LEFT) == 0:
        return LIST_RIGHT
    elif len(LIST_RIGHT) == 0:
        return LIST_LEFT

    # General Case
    INDEX_LEFT = 0
    INDEX_RIGHT = 0
    LIST_MERGE = []
    LIST_LENGTH_TOTAL = len(LIST_LEFT) + len(LIST_RIGHT)
    while len(LIST_MERGE) < LIST_LENGTH_TOTAL: # iterative part of code
        if LIST_LEFT[INDEX_LEFT] <= LIST_RIGHT[INDEX_RIGHT]:
        # checks if the left value is smaller than the right value and places the left value
            LIST_MERGE.append(LIST_LEFT[INDEX_LEFT])
            INDEX_LEFT = INDEX_LEFT + 1
        else:
            # places the right value if bigger
            LIST_MERGE.append(LIST_RIGHT[INDEX_RIGHT])
            INDEX_RIGHT = INDEX_RIGHT + 1

        #Optimization made by yours truly, Mr.Zhang (to check if one list is done
        if INDEX_RIGHT == len(LIST_RIGHT):
            # reached the end of the right list, append the rest of the left list.
            LIST_MERGE = LIST_MERGE + LIST_LEFT[INDEX_LEFT:]
            break
        elif INDEX_LEFT == len(LIST_LEFT):
            # reached the end of the left list, append the rest of the right list.
            LIST_MERGE = LIST_MERGE + LIST_RIGHT[INDEX_RIGHT:]
            break
    return LIST_MERGE

def mergeSort(LIST):
    '''
    performs the recursive split of the list
    :param LIST: list(int)
    :return: list --> sorted
    '''
    if len(LIST) <= 1:
        return LIST # base case
    else:
        MIDPOINT_INDEX = len(LIST)//2
        LEFT = LIST[:MIDPOINT_INDEX]
        RIGHT = LIST[MIDPOINT_INDEX:]
        #The following line is the recursive statement
        return mergeSortedLists(mergeSort(LEFT), mergeSort(RIGHT))

if __name__ == "__main__":
    from myFunctions import *
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        NUMBERS = mergeSort(NUMBERS)
        END_TIME = getTime()
        TIMES.append(END_TIME - START_TIME)
        print(i)
    print(getAverage(TIMES))
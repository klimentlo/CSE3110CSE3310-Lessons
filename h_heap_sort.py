# h_heap_sort.py

'''
title: heap sort algorithm
author kliment lo
date-created: 2023/09/19
'''

def heapify(LIST, LEN_ARRAY, ROOT_INDEX):
    '''
    Heapifies all subtreesin the binary tree
    :param LIST: list(int)
    :param LEN_ARRAY: int
    :param ROOT_INDEX: int -> parent index
    :return:
    '''

    LARGEST_INDEX = ROOT_INDEX
    LEFT_INDEX = 2 * ROOT_INDEX + 1
    RIGHT_INDEX = 2 * ROOT_INDEX + 2

    # Test if left child is larger than the largest index value
    if LEFT_INDEX < LEN_ARRAY and LIST[ROOT_INDEX] < LIST[LEFT_INDEX]:
        LARGEST_INDEX = LEFT_INDEX

    #Test if right child v alue is larger than the largest index value.
    if RIGHT_INDEX < LEN_ARRAY and LIST[LARGEST_INDEX] < LIST[RIGHT_INDEX]:
        LARGEST_INDEX = RIGHT_INDEX

    # Change the ROOT/Parent if needed
    if LARGEST_INDEX != ROOT_INDEX:
        TEMP = LIST[ROOT_INDEX]
        LIST[ROOT_INDEX] = LIST[LARGEST_INDEX]
        LIST[LARGEST_INDEX] = TEMP

        #Heapify the Root
        heapify(LIST,LEN_ARRAY, LARGEST_INDEX)

def heapSort(LIST):
    '''
    sorts the list
    :param LIST: list(int) - >unsorted
    :return: none
    '''

    LEN_ARRAY = len(LIST)

    #build the max heap
    for i in range(LEN_ARRAY, -1, -1): # from tail to head
        heapify(LIST, LEN_ARRAY, i)


    #Extract the highest element
    for i in range(LEN_ARRAY - 1, 0, -1):
        LIST[i], LIST[0] = LIST[0], LIST[i] # swaps index zero with highest value in unsorted section

        heapify(LIST, i, 0)

if __name__ == "__main__":
    from myFunctions import *

    TIMES = []
    for i in range(100):
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        heapSort(NUMBERS)
        END_TIME = getTime()
        TIMES.append(END_TIME-START_TIME)

        print(i)
    print(NUMBERS)
    print(getAverage(TIMES))
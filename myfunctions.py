# myFunctions.py
'''
title: common functions for the unit
author: kliment lo
date: 2023/09/07
'''
import random,  time, statistics

def getSmallList():
    '''
    return a small list of integers
    :return: (list)
    '''

    return [1,5,19,3,11,17,7,13]

def getList(SIZE):
    '''
    return a storted list of approximate size
    :param SIZE: (int)
    :return: (list)
    '''

    numbers = []
    for i in range(2*SIZE):
        if random.randrange(2) == 1:
            numbers.append(i)
        return numbers

def getRandomList(SIZE):
    '''
    return an unordered list of numbers of approximate size, SIZE
    :param SIZE: (int)
    :return: (list)
    '''

    sorted_list = getList(SIZE)
    random.shuffle(sorted_list)

    return sorted_list

def getAverage(TIMES):
    '''
    return the averag eof hte given list
    :param TIMES: (list)
    :return: (float)
    '''

    return statistics.mean(TIMES)

def getTime():
    '''
    return the performance counter time
    :return: (float)
    '''
    return time.perf_counter()

if __name__ == "__main__":
    print(getSmallList())
    print(getList(10))
    print(getRandomList(10))
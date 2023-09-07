#a_linear_search.py

'''
title: a_linear_search.py
author: kliment_lo
date: 2023/09/06
'''

import random
import time
import statistics

### -- Inputs

### -- Processing
# Make a large data set
NUMBERS = []
for i in range(20000000):
    if random.randrange(2) == 1:
        NUMBERS.append(i)

TRIALS = []

for i in range(30):
    # Choose a random number
    NUMBER = NUMBERS[random.randrange(len(NUMBERS))]

    # Search for the chosen value
    START_TIME = time.perf_counter()
    for i in range(len(NUMBERS)):
        if NUMBERS[i] == NUMBER:
            print("found!")
            break #breaks through this while loop
    END_TIME = time.perf_counter()
    TRIALS.append(END_TIME-START_TIME)

### -- Outputs
print(statistics.mean(TRIALS))

print(NUMBER)
print(END_TIME-START_TIME)
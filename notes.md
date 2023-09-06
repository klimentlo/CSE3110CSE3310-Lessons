# notes.md
# CSE3110 - Iterative algorithms
Iterative Algorithms are algorithms that use loops like while and for loops to process large sets of data. In contrast, Recursive Algorithms are algorithms that recall the sam algorithm over and over again to process large sets of data. Recursive algorithms often nest the same algorithm in itself, reducing teh size of the data set until the data set is the smallest possible. While Iterative algorithms tend to be faster than Recursive algorithms, algorithms that use both are even faster

Iterative algorithms are easier to program than recursive algorithms.

In this unit, only search and sort algorithms using numbers are explored.

## Linear Search 
Linear search is the easiest to program, but least efficient method to search. It processes the data line-by-line, similar to brute force decryption algorithms.

```python
FOUND = False
for i in range(len(A_LIST)):
    if VALUE == A_LIST[i]:
     FOUND == True
     break
```

Linear search processing time is dependent on the length of the array and the value's placement within the array. Arrays that are 1000 indices or higher can have a noticeable change in time requirements while running.

### Measuring Time
To measure the processing time within python, the ```time.perf_counter()``` will measure the approximate milliseconds it takes to run the program.

For more accurate results, we use the average of at least 3o trials and then use ```statistics.mean()``` to find the average.
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

## Binary Search
Binary search follows the __divine and conquer__ technique of finding a value. It takes an __ordered__ set of data and tests the midpoint value Then it cuts the list in half and rerun the processes until the value is found.

**Steps for Binary Search**
1. Determine the Midpoint of the list.
2. Test if the Midpoint value is the value that is being searched
   1. If the midpoint value is the searched value, end.
   2. If the value is larger than the midpoint, redefine the lowest index of the list to the one above the midpoint and rerun the search.
   3. If the value is smaller than the midpoint, redefine the highest index of the list to be the midpoint and rerun the search. (Reminder the highest index number in the range is not part of the range)
3. Repeat 1 and 2 until the value is found.

* Advantages of Binary Search
  * It is significantly faster than linear search
* Disadvantages
  * List must already be sorted
  * List must have consistent data that can be represented as integers
  * Harder to program

## Sorting Data
Just like searching algorithms, sorting algorithms have varying levels of efficiency. There are several types of sort algorithms including bubble, selection, insertion, and merge. (Python uses Timsort, which is a hybrid of merge and insertion sort designed by Tim Peters in 2002)

### Bubble Sort
Bubble sort compares two adjacent values on the list and arranges them from lowest to highest. Then it moves to the next index pair and repeats the two value sort until it reaches the end of the unsorted list. The final index is the value that is sorted and the algorithm repeats until each index (traversed tail-to-head) is sorted.


Advantages are that this algorithm requires little memory and is easy to program, but the disadvantages are that its processing time is directly proportional to the length of the data set.

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- 
| 1 | 3 | 5 | 11 | 17 | 7 | 13 | *__19__* |
| 1 | 3 | 5 | 11 | 7 | 13 | *__17__* | 19 |
| 1 | 3 | 5 | 7 | 11 | *__13__* | 17 | 19 |
| 1 | 3 | 5 | 7 | *__11__* | 13 | 17 | 19 |
| 1 | 3 | 5 | *__7__* | 11 | 13 | 17 | 19 |
| 1 | 3 | *__5__* | 7 | 11 | 13 | 17 | 19 |
| 1 | *__3__* | 5 | 7 | 11 | 13 | 17 | 19 |
| *__1__* | 3 | 5 | 7 | 11 | 13 | 17 | 19 |
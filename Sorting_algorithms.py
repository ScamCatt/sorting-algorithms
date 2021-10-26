import time
from sys import setrecursionlimit
from random import shuffle
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

# Edit the recursion limit 
setrecursionlimit(10**6)

# Generate an unsorted list of 50 integers
n = 50
values = list(range(1, 51))
shuffle(values)
print(values)

figure = plt.figure()
window = figure.canvas.manager.window
rects = plt.bar([i for i in range(n)], values)

# Visualize the sorting
def plot_graph(values: list, n = len(values)):
    plt.show()

def update_graph(values):
    for i, rect in enumerate(rects):
            rect.set_height(values[i])
    figure.canvas.draw()
    time.sleep(0.05)

# Selection sort
# Time complexity: O(n^2) (Very Slow)
def selection_sort(values = values, n = len(values)):
    for i in range(0, n-1):
        minpos = i
        for j in range(i, n):
            if values[j] < values[minpos]:
                minpos = j
        values[i], values[minpos] = values[minpos], values[i]
        update_graph(values)

# Bubble sort
# Time complexity: O(n^2) (Also Very Slow)
def bubble_sort(values = values, n = len(values)):
    for i in range(0, n-2):
        flag = 1
        for j in range(0, n-i-1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
                update_graph(values)
                flag = 0
        if flag:
            break
    return values

# Insertion sort
# Time complexity: O(n) in best case, O(n^2) on average case
def insertion_sort(values = values, n = len(values)):
    for i in range(1, n):
        value = values[i]
        hole = i
        while(hole>0 and values[hole-1]>value):
            values[hole] = values[hole-1]
            hole = hole-1
            update_graph(values)
        values[hole] = value
        update_graph(values)
    return values

# Merge sort
# Time complexity: O(nlog(n)) in worst case
# Space complexity: O(n)
def merge(values: list, L, R):
    nL = len(L)
    nR = len(R)
    i, j, k = 0, 0, 0
    while(i < nL and j < nR):
        if(L[i] <= R[j]):
            values[k] = L[i]
            i+=1
        else:
            values[k] = R[j]
            j+=1
        k+=1
    while(i<nL):
        values[k] = L[i]
        k+=1
        i+=1
    while(j<nR):
        values[k] = R[j]
        k+=1
        j+=1

def merge_sort(values = values):
    n = len(values)
    if(n<2):
        return
    L = values[:n//2]
    R = values[n//2:]
    print(L, R)
    merge_sort(L)
    merge_sort(R)
    merge(values, L, R)
    return values

# Quick sort
# Time complexity: O(nlog(n)) on average but O(n^2) in worst case, it is very rare to get a worst case though
# Space complexity: in-place
def partition(values, start, end):
    pivot = values[end]
    pIndex = start
    for i in range(start, end):
        if(values[i]<=pivot):
            values[i], values[pIndex] = values[pIndex], values[i]
            update_graph(values)
            pIndex+=1
    values[end], values[pIndex] = values[pIndex], values[end]
    update_graph(values)
    return pIndex

def quick_sort(values: list, start, end):
    if(start>=end):
        return
    pIndex = partition(values, start, end)
    quick_sort(values, start, pIndex-1)
    quick_sort(values, pIndex+1, end)
    
    return values

def quicksort_start():
    quick_sort(values, 0, 49)

lmao = time.time()
#print(quick_sort(values, 0, len(values)-1))
print(time.time()-lmao)
window.after(0, quicksort_start)
plot_graph(values)

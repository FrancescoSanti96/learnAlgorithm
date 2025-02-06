# SELECTION SORT

def min_index(a, index_from, index_to): 
    min_idx = index_from
    for i in range(index_from+1, index_to):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def selection_sort(a):
    for i in range(len(a)-1):
        min_idx = min_index(a, i, len(a))
        a[i], a[min_idx] = a[min_idx], a[i]


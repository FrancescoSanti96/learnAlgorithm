# QUIK SORT

def partition(a,start,to):
    pivot = a[start]
    k = start+1
    for i in range(start+1,to):
        if a[i] < pivot:
            a[i], a[k] = a[k], a[i]
            k += 1
    a[start] = a[k-1]
    a[k-1] = pivot
    return k-1

# sort array
def quick_sort(array, start=None, to=None):
    start = 0 if start==None else start
    to = len(array) if to==None else to
    if start < to:
        pivot_index = partition(array,start,to)
        quick_sort(array,start,pivot_index)
        quick_sort(array,pivot_index+1,to)
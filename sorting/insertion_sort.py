# INSERTION SORT

def insert_in_order(arr, n, e):
    pos = n
    while pos > 0 and arr[pos-1] > e:
        arr[pos] = arr[pos-1]
        pos -= 1
    arr[pos] = e

def insertion_sort(a):
    for i in range(1,len(a)):
        insert_in_order(a, i, a[i])

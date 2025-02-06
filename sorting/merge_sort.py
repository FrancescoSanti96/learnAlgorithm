# MERGE SORT

def merge(a, b, r):
    i, j, k = 0, 0, 0
    # print(f"merge {a} and {b} into {r}")
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            r[k] = a[i]
            i = i + 1
        else:
            r[k] = b[j]
            j = j + 1
        k = k + 1
    for i in range(i,len(a)):
        r[k] = a[i]
        k = k + 1
    for i in range(j,len(b)):
        r[k] = b[i]
        k = k + 1

def merge_sort(a):
    if len(a)<=1: return
    m = len(a)//2
    left = a[:m] # beware: it's a copy
    right = a[m:] # beware: it's a copy
    merge_sort(left)
    merge_sort(right)
    merge(left, right, a)
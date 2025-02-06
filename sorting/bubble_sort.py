# BUBBLE SORT

def bubble_sort(a):
    swap = True
    n = len(a)
    i = 0
    while swap and i < n-1:
        swap = False
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                swap = True
                a[j], a[j+1] = a[j+1], a[j]
        i += 1
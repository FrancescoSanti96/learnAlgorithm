# RICERCA BINARIA ITERATIVA
def binary_search_iter(array, x, start, to, eq = lambda x, y: x == y, less = lambda x, y: x < y):
    while start <= to:
        m = (start + to) // 2
        if eq(array[m], x): return m
        elif less(array[m], x): start = m+1
        else: to = m-1
    return -1

def binary_search(array, x):
    return binary_search_iter(array, x, 0, len(array)-1)

# RICORSIVA
def binary_search_recur(array, x, start, to, eq = lambda x, y: x == y, less = lambda x, y: x < y):
    if to < start: return -1
    if start == to:
        return start if eq(array[start], x)  else -1
    mid = start + (to - start)//2
    print(f"from={start}; to={to}; mid={mid}")
    if eq(array[mid], x): return mid
    elif less(array[mid], x): return binary_search_recur(array, x, mid+1, to)
    else: return binary_search_recur(array, x, start, mid-1)


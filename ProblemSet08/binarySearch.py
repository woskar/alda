# ALDA Blatt 8 Ulrich Prestel und Oskar Weinfurtner
# Aufgabe 3: Binary Search

def binarySearch(a, key, start, end):
    size = end – start
    if size <= 0:
        return None
    center = (start + end) // 2
    if key == a[center]:
        return center
     elif key < a[center]:
        return binarySearch(a, key, start, center)
    else:
        return binarySearch(a, key, center+1, end)

def binarySearch2(a, key):
    if len(a) == 0:
        return None
    center = len(a) // 2
    if key == a[center]:
        return center
    elif key <  a[center]:
        return binarySearch2(a[:center], key)
    else:
        res = binarySearch2(a[center+1:], key)
        if res is None:
            return None
        else:
            return res + center + 1

import time

"""
print()
print("Messung von fib6(n):")
n = 241050 # Startwert festlegen
while True:
    t_start = time.time()
    value = fib6(n)
    t_end = time.time()
    passed_time = t_end-t_start
    print("N:", n, "fib(N):", value, "time:", passed_time)
    if passed_time > 10:
        break
    n = math.floor(n*1.1)

# Ausgabe:
# N: 241050
# time: 9.740862846374512 s

"""
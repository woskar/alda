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



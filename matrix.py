# ALDA Zettel 4 Aufgabe 3
# Ulrich Prestel und Oskar Weinfurtner

import timeit
import random

size = 100
m1 = [random.random() for _ in range(size*size)]
m2 = [random.random() for _ in range(size*size)]

# Naive Matrix-Multiplikation von zwei size*size Matrizen
def naiv(A, B, C, size):
    for i in range(size):
        for j in range(size):
            for k in range(size):
                C[i + j*size] += A[i + k*size] * B[k + j*size]

# Verbesserte Matrix-Multiplikation
def matmul(A, B, C, size):
    for j in range(size):
        a = j*size # invarianten Ausdruck nach außen verlagern
        for i in range(size):
            b = i + a # zweite Invariante auslagern
            for k in range(size):
                C[b] += A[i + k*size] * B[k + a]

# Zeit messen mit timeit:

initialisation='''
C = [0] * (size*size)
'''

code_to_be_measured='''
matmul(m1, m2, C, size)
'''

repeats = 10
N = 400
t = timeit.Timer(code_to_be_measured, initialisation, globals=globals())

# Eigentliche Zeitmessung:
time = t.timeit(repeats)
print("average execution time:", time/repeats)

# Zeit durch obige Maßnahmen verbessert von 0.355 sec auf 0.247 sec

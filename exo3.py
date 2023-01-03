import numpy as np
import matplotlib.pyplot as plt

n = 5

A = np.zeros((n,n))
for i in range(n):
    A[i,i] = i+1

print("A = ")
print(A)

def f(x):
    y = x**3
    return y

print(f(np.arange(4)))
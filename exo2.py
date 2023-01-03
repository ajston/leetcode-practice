import numpy as np
import matplotlib.pyplot as plt

n = 4

A = np.empty((n,n))
for i,j in range(n,n):
    if(i!=j):
        A[i,j] = 2
    else:
        A[i,j] = 1

B = np.empty((n,n))
for i,j in range(n,n):
    B[i,j] = j

print("A = ")
print(A)

print ("\n $$$$ \n ")

print("B = ")
print(B)
import numpy as np
import matplotlib.pyplot as plt

## Initiation à la programmation en Python pour l'analyse numérique

## Exercice 1 : Manipulation des vecteurs et des matrices

# Creation de listes
liste1 = [1, 2, 3, 4, 5]
liste2 = [[11, 12] , [21, 22]]
liste3 = ['toto' , 1 , 4.0]

# Définition de vecteurs et matrices
x = np.array([1, 2, 3])
y = np.array([[4], [5], [6]])
z = np.array([[1, 2], [3, 4]])

# Matrices et vecteurs particuliers
v1 = np.zeros(3)
v2 = np.ones(2)
identite1 = np.eye(5, 4)
identite2 = np.eye(4, k=-1)
identite3 = np.diag(v2)
identite4 = np.diag(v2, k=-1)
zz = np.zeros((2,3))
sizez = (np.size(z,0), np.size(z,1))
zzz = np.zeros(sizez)
un = np.ones((2,2))

# Extraction de coefficients
print(x[0])
print(x[-1])
print(z[0,1])
print(x[1:3])
print(z[:,1])
print(np.diag(z))

# Opérations d'algèbre linéaire
print(np.transpose(z))
print(z.T)
print(np.linalg.matrix_power(z,2))
print(z+un)
print(z.dot(un))
print(np.linalg.inv(z))

# Operations coefficients par coefficients
print(z*z)
print(1/z)
print(z+1)


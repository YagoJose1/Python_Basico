import numpy as np

#criando a matriz 3x3
matriz = np.array([[1 , 2 , 3],[4 , 5 , 6],[7 , 8 , 9 ]])

#selecionando valores da matriz
print(matriz)
print(matriz[1 , 2 ])

#modificando valores da matriz
matriz[0 , 2] = 10
print(matriz)
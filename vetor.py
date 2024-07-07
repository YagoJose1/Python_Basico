#Vetor usando numpy

import numpy as np

#criaçao do vetor

vetor = np.array([3, 5, 10, 2, 8])

#modificando valores

vetor[1] = 7

#operacao vetoriais

vetor = vetor + 3

#dizendo o tamanho do vetor

#print(len(vetor))

#operacoes matematicas

soma = np.sum(vetor)
media = np.mean(vetor)
produto = np.prod(vetor)

print(vetor)
print("Soma : ", soma, " Média : ", media, " Produto : ", produto)
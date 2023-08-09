# Prática 20 - 26/05/23
#  matrizes

# Pratica 2 - Crie um programa que conte quantos números '0' (zeros) tem na matriz:
import numpy as np
matriz = np.empty((2, 2),dtype=float)
cont = 0   #contador
for i in range (2):    #para a matriz ser dinamica com o usuario é só fazer outro for
    for j in range (2):
        valor =  int(input('Digite o valor para o elemnto[(i)][(j)]'))
        matriz[i][j] = valor
        if matriz[i][j] == 0:    #if pra perguntar se o numero atribuido está na matriz
            cont = cont  + 1     # cada vez que aparecer um zero ele vai contar
print(matriz)
print('O número de zeros na matriz é: ', cont)


#                  CONTINUAÇÃO DOS EXERCICIOS - 29/05/23

#  Pratica 3 - Crie um programa que retorne a soma de todos os elementos de uma matriz: 
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]   #definir uma matriz com valoores.
#calcula a soma de todos os elementos da matriz.
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        soma += matriz [i][j]
print ('A soma dos numeros da matriz é', soma)
    

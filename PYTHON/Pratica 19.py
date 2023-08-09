#Prática 19 - 25/05/23  - MATRIZES 

# Pratica 1 - Faça um programa que pergunte ao usuario quantas linhas e quantas colunas deve ter a matriz, e também pergunte cada elemento a ser inserido na mesma:
import numpy as np   
linhas = int(input('Qual o valor de linhas? '))
colunas = int(input('Qual o valor de colunas? '))
matriz = np.empty((linhas, colunas))
print(matriz)

# Resposta para a pratica 1
import numpy as np
linhas = int(input('Qual o valor de linhas? '))
colunas = int(input('Qual o valor de colunas? '))
matriz = np.empty((linhas, colunas))
#Preenchendo a matriz com valores fornecidos pelo usuario:
for i in range (linhas):
    for j in range (colunas):
        valor =  int(input('Digite o valor para o elemnto[(i)][(j)]'))
        matriz[i][j] = valor

print(matriz)

#mostrar elemento por elemento:
for i in range (linhas):
    for j in range (colunas):
        print(matriz[i][j], end= ' ')
    print( )












#25/05/23
#                 MATRIZES

# O ideal é usar float em matrizes
# estrutura alinhada quando usamos for em matrizes.


#   Criando uma matriz em python:
import numpy as np              #dando um apelido para a biblioteca  #apelido dado np
#criando uma matriz 2x3
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)

import numpy as np   
#   Criando uma matriz 3x3
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)

#   Criando uma matriz com uma matriz vazia:
import numpy as np   
matriz_vazia = np.empty((3, 3))
#preenchendo a matriz usando uma lista vazia   #matriz 3x3 #primeiro colchetes LINHA, segundo colchetes COLUNA
matriz_vazia[0][0] = 1
matriz_vazia[0][1] = 1
matriz_vazia[0][2] = 1
matriz_vazia[1][0] = 1
matriz_vazia[1][1] = 1
matriz_vazia[1][2] = 1
matriz_vazia[2][0] = 1
matriz_vazia[2][1] = 1
matriz_vazia[2][2] = 1
print(matriz_vazia)

#   Criando matrizes só com zeros:
import numpy as np  
m = np.zeros((4,4), dtype = float)
print(m)


#                    CONTINUAÇÃO DE MATRIZES - 29/05/23

# Exemplos:
import numpy as np
m = np.empty((2, 2), dtype = float)   # dtype é um tipo de variavel, neste caso float
cont = 0
listapares = []   # selicionando em uma lista apenas os numeros pares  
for linhas in range (2):
    for colunas in range (2):
        numero =  float(input('Digite um número: '))
        m[linhas][colunas] = numero
        if m[linhas][colunas] == 0:    # checando a contagem de zeros
                cont = cont + 1   
        if m[linhas][colunas] % 2 == 0:
                listapares.append(m[linhas][colunas])
print (m)
print (cont)
print (listapares)


#                CONTINUAÇÃO DE MATRIZES   - 30/05/23

import numpy as np
m = np.empty   
cont = 0
listapares = [] 
for linhas in range(2):
    for colunas in range (2):
        numero = float(input('Digite um numero: ['+str(linhas)+']'+'['+str(colunas)+']'))
        m[linhas][colunas] = numero


#Pratica 18 - 23/05/23 - CONTINUAÇÃO DE LISTAS

#Pratica 8 - Escreva um programa que receba uma lista de números e retorne outra lista contendo apenas os números que são divisíveis por 3 ou por 5:
numeros  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisiveis = []
for numero in numeros:
    if numero % 3 == 0 or numero % 5 == 0:
        divisiveis.append(numero)
print('Os números divisiveis por 3 e 5 são ', divisiveis)

#Prática 9 - Escreva um programa que receba duas listas e retorne uma nova lista contendo apenas os elementos comuns ás duas listas:
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [2, 4, 6, 8, 10, 12]
comuns = []
for elemento in lista1:
    if elemento in lista2:
        comuns.append(elemento)
print('Os elementos comuns nas listas são ', comuns) 

#Prática 10 - Escreva um programa que receba uma lista de números e retorne a soma de todos os números ímpares da lista:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0
for numero in numeros:
    if numero % 2 != 0:
        soma += numero
print(soma)


#                            TUPLAS - 23/05/23
# o que é? Uma lista que não muda
# A mesma coisa que uma lista só que se usa parenteses, ex:
tupla1 = (1, 2, 3)

#Prática 14 - Encontre o valor maximo e minimo:
#minimo
tupla = (3, 1, 4, 2)
valor_minimo = min(tupla)
print(valor_minimo)
#maximo
tupla = (3, 1, 4, 2)
valor_maximo = max(tupla)
print(valor_maximo)




   
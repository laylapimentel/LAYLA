#                  funções das listas

#função count
#procura o numero repetido, pode ser usado em string, só verifica uma lista e dá os números 
lista = [1, 2, 3, 2]
contador = lista.count(2) 
print(contador)     #resultado 2

#função len
#quantidade de elmentos que tem na lista
lista = [3, 1, 4, 2]
comprimento = len(lista)
print(comprimento)    #resultado 4

#ordenar lista
#função sort
lista = [4, 3, 1, 2]
lista.sort()
print(lista)  #resultado = [1, 2, 3, 4]

#funçao reverse 
lista = [1, 2, 3, 4]
lista.reverse()
print(lista)  #resultado [4, 3, 2, 1]

#função min(lista)
lista = [3, 1, 4, 2]
valor_minimo = min(lista)
print(valor_minimo)  #resultado 5

#função max(lista)
lista = [3, 1, 4, 2]
valor_maximo = max(lista)
print(valor_maximo) #resultado 4

#função slice em listas 
# retirar uma parte da lista, ou seja, somente a parte desejada 
lista = [10, 20, 30, 40, 50, 60]
print(lista[2:5])      #resultado [30, 40, 50, 60] 
#Pratica 17
#aula do dia 19/05/23, exercicios de listas
#PRATICA 3 - Escreva um programa que receba uma lista de 5 nbumeros e retorne a soma de todos os numeros.
lista = []
for elemneto in range(5):  #qualquer coisa colocada em for é um elemento, ex: elemento    #in significa em
    n = int(input('Digite um número: '))
    lista.append(n) 
soma = sum(lista)       #A função sum (função de soma) vai somar todos os elementos da lista
print(soma)

#Para digitar o número de vezes que o usuario deseja, é só declarar uma variavel que o programa perguntará o numero de vezes que você deseja:
lista = []
num = int(input('Digite a quantidade de números: '))
for elemneto in range(num):
    n = int(input('Digite um número: '))
    lista.append(n)
soma = sum(lista)
print(soma)

#A soma dentro do for irá somar o numero digitado com o anterior:
lista = []
num = int(input('Digite a quantidade de números: '))
for elemneto in range(num):
    n = int(input('Digite um número: '))
    lista.append(n) 
    soma = sum(lista)
    print(soma)

#Multiplicar a lista por 2:
lista = []
num = int(input('Digite a quantidade de números: '))
for elemneto in range(num):
    n = int(input('Digite um número: '))
    lista.append(n) 
soma = sum(lista) * 2
print(soma)

#PRATICA 4 - Escreva um programa que receba uma lista de números e retorne a soma de todos os numeros dividida por 2:
lista = []
num = int(input('Digite a quantidade de números: '))
for elemneto in range(num):
    n = int(input('Digite um número: '))
    lista.append(n/2)
    soma = lista
    print(soma)

#escreva um programa que receba uma lista de 3 inteiros via teclado, em seguida o programa deve solicitar um número e informa se o número também está na lista ou não:
lista = []
for elemneto in range(3):
    n = int(input('Digite um número: '))
    lista.append(n)
num = int(input('Digite um número novamente: '))
if num in lista:
    print('o número está na lista')
else:
    print('O número não está na lista')


#PRATICA 7 - Escreva um programa que leia 4 números via teclado, tire a média e mostre o resultado na tela:
lista = []
for elemneto in range(4):
    n = int(input('Digite um número: '))
    lista.append(n)
soma = sum(lista)
media = soma / 4
print('A média dos elementos da lista é ', media)



# Aula do dia 23/05/23

#                       TUPLAS:

# O que é? Uma lista que não muda
# Usamos as mesmas funçoes de listas
# A mesma coisa que uma lista só que se usa parenteses, ex:
tupla1 = (1, 2, 3)


#                DICIONARIOS EM PYTHON:

dicionario = {'nome': 'Joao', 'idade': 30, 'cidade': 'São Paulo'}
print(dicionario['nome'])        #saida: Joao
print(dicionario['idade'])       #saida: 30
print(dicionario['cidade'])      #saida: São Paulo


# Inserindo valores em um dicionario:
dicionario = {'nome': 'Joao', 'idade': 30}
(dicionario['cidade']) = 'São Paulo'   #Adiciona uma nova chave-valor         
(dicionario['idade']) = 31             #chamando a chave novamente e atualizando o dicionario


# Deletando valores em um dicionario:
dicionario = {'nome': 'Joao', 'idade': 30, 'cidade': 'São Paulo'}
del dicionario['idade']          #removendo a chave-valor 

# Percorrendo um dicionario:
dicionario = {'nome': 'Joao', 'idade': 30, 'cidade': 'São Paulo'}
for chave, valor in dicionario.items():
    print(chave, valor)


#               CONTINUAÇÃO DA AULA ANTERIOR - DICIONARIOS  
# Aula do dia 224/05/23


# Verificando existencia uma chave em um dicionario
dicionario = {'nome': 'Joao', 'idade': 30}
existe_chave in dicionario
#incompleto


# Obtendo as chaves e os valores de um dicionario
dicionario = {'nome': 'Joao', 'idade': 30, 'cidade': 'São Paulo'}
chaves = dicionario_keys
valores = 
#incompleto

# Comprimento de um dicionario
dicionario = {'nome': 'Joao', 'idade': 30, 'cidade': 'São Paulo'}
comprimento = len(dicionario)
print(comprimento)             #saida = 3

# Usando um dicionario existente como fonte de dados
dados = {'a' : 1, 'b' : 2, 'c' : 3}
dicionario {}
for chave in dados.items():
    dicionario[chave] = valor 
print(dicionario)              #saida = {'a' : 1, 'b' : 2, 'c' : 3}


# Usando uma lista de chaves e um valor comum para todas as chaves:
chaves = ['a', 'b', 'c']
valor_comum = 0
dicionario {}
for chave in chaves:            #adicionaria um input aqui
    dicionario[chave] = valor_comum
print(dicionario)               #saida chaves {'a' = 0, 'b' = 0, 'c' = 0}


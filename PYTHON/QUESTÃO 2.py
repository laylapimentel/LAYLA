def num_pares(lista):
    num_pares = []
    
    for num in lista:
        if num % 2 == 0:
            num_pares.append(num)
            
    return num_pares

minha_lista = [0, 3, 6, 9, 12, 15, 18, 21, 24]
pares = num_pares(minha_lista)

print("Os números pares da lista são: ", pares)

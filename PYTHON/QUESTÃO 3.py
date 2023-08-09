def contar_digitos(num):
    numero_str = str(num)
    qtd_digitos = len(numero_str)
    
    return qtd_digitos

num = int(input("Digite um número inteiro: "))
quantidade = contar_digitos(num)

print("Quantidade de dígitos:", quantidade)

def cal_potencia(a, b):
    result = a ** b
    
    return result

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
potencia = cal_potencia(base, expoente)

print("Resultado:", potencia)


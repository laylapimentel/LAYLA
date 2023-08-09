def cal_gorjeta(valor_conta):
    gorjeta = valor_conta * 0.1
    
    return gorjeta

valor_conta = float(input("Digite o valor da conta: "))
gorjeta = cal_gorjeta(valor_conta)

print("A gorjeta do garçom é o valor de R$", gorjeta)

def op_mat(n1, n2):
    
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2
    
    print("A soma dos números é:", soma)
    print("A subtração dos números é:", subtracao)
    print("A multiplicação dos números é:", multiplicacao)
    print("A divisão dos números é:", divisao)

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

op_mat(numero1, numero2)

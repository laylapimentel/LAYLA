# Exercicio dos salarios
salario = float(input('Digite seu sálario: '))
if salario < 280:
    reajuste = salario * 0.2
    salario_novo = reajuste + salario
    print('Sálario antigo: ', salario)
    print('sálario novo: ', salario_novo)
    print('percentual aplicado: 20%')
    print('valor do aumento: ', reajuste) 
    
if salario >= 280 and salario < 700:
    reajuste = salario * 0.15
    salario_novo = reajuste + salario
    print('Sálario antigo: ', salario)
    print('sálario novo: ', salario_novo)
    print('percentual aplicado: 15%')
    print('valor do aumento: ', reajuste)
    
if salario >= 700 and salario < 1500:
    reajuste = salario * 0.1
    salario_novo = reajuste + salario
    print('Sálario antigo: ', salario)
    print('sálario novo: ', salario_novo)
    print('percentual aplicado: 10%')
    print('valor do aumento: ', reajuste)

if salario > 1500:
    reajuste = salario * 0.05
    salario_novo = reajuste + salario
    print('Sálario antigo: ', salario)
    print('sálario novo: ', salario_novo)
    print('percentual aplicado: 5%')
    print('valor do aumento: ', reajuste)
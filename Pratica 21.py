# Pratica 21  -  30/05/23  -     FUNÇÕES

# pratica 1 - crie uma função que some dois numeros:
def somar(n1, n2):
    resultado = n1 + n2
    return resultado
print(somar(2,2))

# Função pra criar a média de 3 notas
def medianotas(n1, n2, n3):
    m = (n1 + n2 + n3) / 3 
    return m 
print(medianotas(8, 6, 9))  #pode adicionar as notas diretamente aqui, sem a necessidade de pedir ao usuario
#para dizer se o aluno foi reprovado ou aprovado, basta fazer um if.

# Pratica 2 - Crie uma função que calcule a area do triangulo:
def area(base, altura):
    resultado = (base * altura) / 2
    return resultado   #esse return é opcional
print(area(5, 6))
#declarando uma variavel
def area(base, altura):
    r = (base * altura)/ 2
    return r
x = area(5, 6)
print(x)


#             CONTINUAÇÃO DE FUNÇÕES  -  31/05/23

# Pratica 3 - Crie uma função que resolva uma equação do sengundo grau:
import math

def equacaosegundograu(a, b, c):
    delta = b**2 - 4 * a * c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    
    elif delta == 0:
        x = -b / (2*a)
        return x
    
    else:
        return "A equação não possui raízes reais."
    
a = 1
b = 3
c = 10

raizes = equacaosegundograu(a, b, c)
print(raizes)

# Uma função para colcular se é maior de idade:
def idade( i ):
    if i < 18:
        print('Você é menor de idade')
    elif i >= 18 and i < 60:
        print('Você é adulto')
    else:
        print('Você é idoso')
idade(19)

# Pra checar se a função é par ou impar:
def função( f ):
    if f % 2 == 0:
        print('A função é par')
    else:
        print('A função é impar')
função(3)



#             CONTINUAÇÃO DE FUNÇÕES  -  05/06/23

# Pratica 4 - crie uma função que receba 3 notas e ao final diga se o aluno esta reprovado ou aprovado, a media é 7:
import math
def notas(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media < 7:
        print('você está reprovado, sua foi', media)
    else:
        print('Você está aprovado! Sua nota foi', media)
notas(8, 8, 8)

# Pratica 5 - Crie uma função que pergunte quanto você ganha por hora e o numero de foras trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês:
import math
def ganhos ():
    ganhoshora = float(input('Quanto você ganha por 1h de trablho?'))
    horastrabalhadas = int(input('Quantas horas você trabalha por mês?'))
    ganhosmes = ganhoshora * horastrabalhadas
    print(ganhosmes)
ganhos()

# Pratica 6 - Faça uma função que peça temperatura em graus Fahrenheit, transforme em Graus Celsiius.
# C = 5 * ((F - 32) / 9)
import math
def temperatura ():
    F =  float(input('Digite a temperatura em Fahrenheit: '))
    c = 5 * ((F - 32) / 9)
    print('A temperaruta em Graus celsius é,', c)
temperatura()


# Pratica 7 - Tendo como dado de entrada altura (h) de uma pessoa, construa uma função que calcule seu peso ideal, utilizando as seguites formulas:
# para homens: (72.7 * h) - 58
# para mulheres (62.1 * h) - 44.7
def pesoideal ():
    h = float(input('Qual sua altura? '))
    genero = input('Qual o seu ganero? Digite (F) para feminino, e (M) para masculino: ')
    if genero == 'F':
        F = (62.1 * h) - 44.7
        print('Seu peso ideal é ', F, 'kg')
    elif genero == 'M':
        M = (72.7 * h) - 58
        print('Seu peso ideal é', M, 'kg')
    else:
        print('Invalido!!!')
pesoideal()



#             CONTINUAÇÃO DE FUNÇÕES  -  06/06/23

# Pratica 9 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime as perguntas são:
# 1. "Telefonou para a vitima?"
# 2. "Esteve no local do crime?"
# 3. "Mora perto da vitima?"
# 4. "Devia para a vitima?"
# 5. "Já trabalhou com a vitima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. se a pessoa responder positivamente a 2 questões ela deve ser classificada como 
#"Suspeita", entre 3 e 4 como cumplice e 5 como "Assassino". Caso contrario, ele será classificado como "Inocente".
def crime():
    print('Respoda sim ou nao para as questões a seguir. ')
    r = []
    p1 = input('Telefonou para a vitima?')
    r.append(p1)
    p2 = input('Esteve no local do crime?')
    r.append(p2)
    p3 = input('Mora perto da vitima?')
    r.append(p3)
    p4 = input("Devia para a vitima?")
    r.append(p4)
    p5 = input("Já trabalhou com a vitima?")
    r.append(p5)
    sim = r.count('sim')
    if sim == 2:
        print('Você é um suspeito do crime!')
    elif sim == 3 or sim == 4:
        print('Você é um cumplice do crime!')
    elif sim == 5:
        print('Você é o assassino!')
    else:
        print('Você é inocente!')
crime()


# Pratica 12 - Criando um sistema de cadastro de funcionarios.
funcionarios = {}

def cadsatrar_funcionario():
    nome = input('Digite o nome do funcionario: ')
    idade = input('Digite a idade do funcionario: ')
    cargo = input('Digite o cargo do funcionario: ')
    salario = input('Digite o salario do funcionario: ')
    
    funcionario = {
        'nome': nome,
        'idade': idade,
        'cargo': cargo,
        'salario': salario
    }
    
    funcionarios [nome] = funcionario
    print('Funcionario cadastrado com sucesso!')
    
# Função para exibir os dados dos funcionarios
def exibir_funcionario():
    nome = input('Digite o nome do funcionario: ')
    
    if nome in funcionarios:
        funcionario = funcionarios[nome]
        print('Dados do funcionario: ')
        print('nome:', funcionario['nome'])
        print('idade:', funcionario['idade'])
        print('cargo:', funcionario['cargo'])
        print('salario:', funcionario['salario'])
        
    else:
        print('funcionario não encontrado') 

# Função para exibir todos os dados dos funcionarios
def exibir_funcionarios():
    if funcionarios:
        print('Lista de funcionarios: ')
        for nome, funcionario in funcionarios.items():
            print('Nome:', funcionario['nome'])
            print('Idade:', funcionario['idade'])
            print('Cargo:', funcionario['cargo'])
            print('Salario:', funcionario['salario'])
            print('-------------------------')
    else:
        print('Não há funcionarios cadastrados!')








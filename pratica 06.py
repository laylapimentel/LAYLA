nome = input('Digite o nome da aluna: ')
cod = input('Digite o codigo da aluna: ')
disci = input('Digite o código da disciplina: ')

n1 = float(input('Digite a Primeira nota: '))    
n2 = float(input('Digite a Segunda nota: '))
n3 = float(input('Digite a Terceira nota: '))

# Checagem de validade das notas 
if n1 > 10 or n2 > 10 or n3 > 10:
    print('Nota invalida')

soma = n1 + n2 + n3

media = soma/3

if soma >= 21 and soma <=29.9:
    print('Parabéns! Você está aprovada.')

if soma >= 15 and soma < 21:
    print('Aluna de Prova Final')
    final = float(input('Digite sua Nota Final: '))
    mediafinal = (media + final)/2
    if mediafinal >= 5:
        print('Aprovada na Final!')
    else:
        print('Aluna Reprovada!')

if soma < 15:
    print('Reprovada direto')
    
if soma == 30 :
    print('Parabéns. Você atingiu a nota maxima!')
    
print('Nome da aluna: ', nome)
print('Código da aluna: ', cod)
print('Disciplina da aluna: ', disci)


def pesoideal ():
    h = float(input('Qual sua altura? '))
    genero = input('Qual o seu ganero? Digite (F) para feminino, e (M) para masculino: ')
    
    F = (62.1 * h) - 44.7
    M = (72.7 * h) - 58
    
    if genero == F:
        print('Seu peso ideal é ', F, 'kg')
        
    elif genero == M:
        print('Seu peso ideal é', M, 'kg')
        
    else:
        print('Invalido!!!')

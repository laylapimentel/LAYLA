#15/05/23 - pratica do profesor

senha = input('Digite sua senha: ')
tentativas = 0

while senha != 123 and tentativas < 3:
    tentativas += 1 
    print('Senha incorreta, tente novamente')
    senha = input ('Digite sua senha novamente: ')
    
if senha == 123:
    print('Senha correta!')
else:
    print('Número de tentativas excedidas!!!')
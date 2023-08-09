def cal_media(*args):
    soma = sum(args)
    media = soma / len(args)
    
    return media

resultado = cal_media(10, 20, 30,)

print("A média é:", resultado)
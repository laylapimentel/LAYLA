def exibir_info (**kwargs):
    
    for chave, valor in kwargs.items():
        
        print(f"{chave}: {valor}")

exibir_info (nome= "Layla", idade = 22, cidade = "São Luis")

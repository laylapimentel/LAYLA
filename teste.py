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

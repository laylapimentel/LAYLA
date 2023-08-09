# Pratica do dia 12/06/23

#Pratica 1 -  Navegue até a pasta de documentos e crie uma nova pasta chamada meus_projetos, reotrne a pasta documentos e crie outra pasta chamada meus_trabalhos.

#                    CONTINUAÇÃO DA AULA DE PROGRAMAÇÃO ORIENTADA A OBJETO - 19/06/23:

# PRATICA - Dizer se o aluno está aprovado ou reprovado
class Alunos:
    def __int__(self, nome):
        self.nome = nome 
        self.notas = []
    def add_notas(self, notas):
        self.notas.append(notas)
    def cal_media(self):
        total = sum (self.notas)
        media = total / len(self.notas)
        return media
    def ver_situacao(self):
        media = self.cal_media()
        if media >= 7:
            return 'Aprovado!'
        elif media >= 6.9:
            return 'Recuperação'
        else:
            return 'Reprovado!'
        
# Criadno uma superclasse:
class Animal:
    def __int__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
    def fazer_barulho(self):
        print('O animal fez barulho!')
        
class Cachorro(Animal):
    def __int__(self, nome, idade, raca):
        super().__init__(nome, idade)       # Se quiser trablhar apenas com nome pode.
        self.raca = raca                  # Raça é um atributo desta classe, por isso é usada só aqui.
    def abana_rabo(self):
        print('Abanando o rabo.')
        
class Gato(Animal):
    def ronronar(self):
        print('O', self.nome,'esta ronronando.')
        


    
        
        
    
    
    
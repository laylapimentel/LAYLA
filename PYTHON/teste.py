

        

class Animal:
    def __int__(self,nome,idade):
        self.nome = nome 
        self.idade = idade
    def fazer_barulho(self):
        print('O animal fez barulho!')
        
class Cachorro(Animal):
    def __int__(self,nome,idade,raca):
        super().__init__(nome,idade)      
        self.raca = raca                 
    def abana_rabo(self):
        print('Abanando o rabo.')
        
class Gato(Animal):
    def _
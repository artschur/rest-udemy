
class Pessoa():
    def __init__(self, nome, idade: int):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def multiplicarIdade(self, multiplicador: int):
        return self.nome() * multiplicador


Art = Pessoa('Arthur', 18)
print(Art.multiplicarIdade(2))
print(Art)



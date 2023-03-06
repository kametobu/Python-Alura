class Estudos():
    def __init__(self):
        self.__senha = 123

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self,valor):
        print("Sem Permissão")

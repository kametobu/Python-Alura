import random
class CodigoProduto():
    def __init__(self,code):
        self.__code = [random.randint(0,x) for x in range(7)]
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self,*args):
        print("Code não pode ser alterado")

class Leite(CodigoProduto):
    def __init__(self, code, dadosNutri):
        super().__init__(code)
        self.Nutri = dadosNutri
    

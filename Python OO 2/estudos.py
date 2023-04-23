from abc import ABCMeta, abstractclassmethod
from random import randint

class View_Info_Func(metaclass = ABCMeta):
    @abstractclassmethod
    def __str__(self):
        pass

class Cadastro_Funcionario(View_Info_Func):
    def __init__(self,nome,cpf):
        self.__nome = nome.title()
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def cartao(self):
        return self._cartao
    
    @nome.setter
    def nome(self,valor):
        self.__nome = valor.title()

    @cpf.setter
    def cpf(self,valor):
        print("Valor não pode ser alterado")

    @cartao.setter
    def cartao(self,valor):
        print("Valor não pode ser alterado")

    def __str__(self):
        return f"Nome: {self.nome} - RA: {self.cpf} - Cartão: {self.cartao}"
  

class Cartao_acesso_jr(Cadastro_Funcionario):
    def __init__(self,nome,cpf):
        super().__init__(nome,cpf)
        self._cartao = "Junior"
    
class Cartao_acesso_pleno(Cadastro_Funcionario):
    def __init__(self,nome,cpf):
        super().__init__(nome,cpf)
        self._cartao = "Pleno"

class Cartao_acesso_senior(Cadastro_Funcionario):
    def __init__(self,nome,cpf):
        super().__init__(nome,cpf)
        self._cartao = "Senior"

if __name__ == "__main__":
    func_1 = Cartao_acesso_jr("alann", "1")
    print(func_1)
    func_2 = Cartao_acesso_pleno("luan", "2")
    print(func_2)
    func_3 = Cartao_acesso_senior("murilo", "3")
    print(func_3)
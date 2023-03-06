class Animais():
    def __init__(self):
        self.__tipo = ""
        self.__raca = ""
        self.__cor = ""
        
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def raca(self):
        return self.__raca
    
    @property
    def cor(self):
        return self.__cor

    @tipo.setter
    def tipo(self,valor):
        self.__tipo = valor
        print(f"Tipo ==> {valor}")
    
    @raca.setter
    def raca(self,valor):
        self.__raca = valor
        print(f"Raça ==> {valor}")
    
    @cor.setter
    def cor(self,valor):
        self.__cor = valor
        print(f"Cor ==> {valor}")

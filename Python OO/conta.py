

class Conta():
    def __init__(self,numero,titular,saldo,limite,*args,**kargs):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def deposito(self,valor):
        self.__saldo += valor
    def saque(self,valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite.")
    def __pode_sacar(self,valor_saque):
        valor_dis_saque = self.__limite + self.__saldo
        return valor_saque <= valor_dis_saque
    def extrato(self):
        print(self.__saldo)
    def Transferencia(self,valor,destino):
        self.__saldo -= valor
        destino._Conta__saldo += valor
        print(f"Tranferencia: {valor}")
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    @property
    def numero(self):
        return self.__numero

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    @limite.setter
    def limite(self,limite):
        self.__limite = limite

@classmethod(Conta) 
def eh_inadimplente(cliente):
    inadimplente = cliente._Conta__saldo < 0.0
    return inadimplente

conta = Conta(123,"Alann",50.0,1000.0)
conta2 = Conta(321,"Luan",50.0,1000.0)

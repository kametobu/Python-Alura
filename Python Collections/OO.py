from abc import ABCMeta,abstractclassmethod
from operator import attrgetter
from functools import total_ordering

class Conta(metaclass=ABCMeta):
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self,valor):
        self._saldo += valor
    
    @abstractclassmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f"[Codigo {self._codigo} Saldo {self._saldo}]"

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.05

#@total_ordering
class ContaSalario:
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self,valor):
        self._saldo += valor

    def __str__(self):
        return f"[Codigo {self._codigo} Saldo {self._saldo}]"

    def __eq__(self, conta):
        if not isinstance(conta, ContaSalario):
            return False
        return conta._codigo == self._codigo and self._saldo == conta._saldo
    
    def __lt__(self, conta):
        if self._saldo != conta._saldo:
            return self._saldo < conta._saldo
        return self._codigo < conta._codigo

    def __le__(self,conta):
        if self._saldo <= conta._saldo:
            return self._codigo <= conta._codigo
        return self._codigo <= conta._codigo
    
conta_alann = ContaSalario(133)
conta_alann.deposita(500)

conta_luan = ContaSalario(3)
conta_luan.deposita(2000)

conta_murilo = ContaSalario(133)
conta_murilo.deposita(500)

class ContaMultiploSalario(ContaSalario):
    pass

conta1 = ContaCorrente(1)
conta1.deposita(1000)
conta1.passa_o_mes()
print(conta1)

conta2 = ContaPoupanca(2)
conta2.deposita(1000)
conta2.passa_o_mes()
print(conta2)

conta1 = ContaCorrente(1)
conta1.deposita(1000)

conta2 = ContaPoupanca(2)
conta2.deposita(1000)

contas = [conta1,conta2]

for conta in contas:
    print(conta)

for conta in contas:
    conta.passa_o_mes()

for conta in contas:
    print(conta)

conta5 = ContaInvestimento(5)
print(conta5)

conta1 = ContaCorrente(6)

conta6 = ContaSalario(6)
print(conta6)

conta7= ContaSalario(6)
print(conta7)

print(conta6 == conta7)

contas = [conta6]

print(conta6 in contas)
print(conta7 in contas)

print(conta6 == conta1)

conta8 = ContaMultiploSalario(6)

print(isinstance(conta5, ContaSalario))

print(conta6 == conta8)

conta_alann = ContaSalario(13)
conta_alann.deposita(500)

conta_luan = ContaSalario(3)
conta_luan.deposita(2000)

conta_murilo = ContaSalario(133)
conta_murilo.deposita(500)

contas = [conta_alann,conta_luan,conta_murilo]

for conta in contas:
    print(conta)

def extrai_saldo(conta):
    return conta._saldo

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

for conta in sorted(contas):
    print(conta)

for conta in sorted(contas, key=attrgetter("_saldo","_codigo")):
    print(conta)

for conta in sorted(contas):
    print(conta)

print(conta_alann <= conta_luan)
print(conta_alann <= conta_murilo)
print(conta_alann <= conta_alann)
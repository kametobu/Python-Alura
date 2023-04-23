class ContaCorrente():
    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self,valor):
        self.saldo += valor

    def __str__(self):
        return f"[Codigo {self.codigo} Saldo {self.saldo}]"
    
if __name__ == "__main__":
    conta1 = ContaCorrente(15)
    print(conta1)
    conta1.deposita(500)
    print(conta1)
    conta2 = ContaCorrente(47685)
    conta2.deposita(1000)
    print(conta2)

    contas = [conta1,conta2]
    print(contas)
    for conta in contas:
        print(conta)
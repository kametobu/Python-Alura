
def cria_conta(numero,titular,saldo,limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta,valor):
    conta["saldo"] += valor
    return conta

def saque(conta,valor):
    conta["saldo"] -= valor
    return conta

def extrato(conta):
    print("Saldo é {0}".format(conta["saldo"]))


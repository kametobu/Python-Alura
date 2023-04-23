from collections import Counter,defaultdict

usuarios = [15,23,43,56]

usuarios2 = [13,23,56,42]

lista_usuarios = usuarios.copy()

lista_usuarios.extend(usuarios2)

print(lista_usuarios)
lista_usuarios_inique = set(lista_usuarios)

print(lista_usuarios_inique)

usuarios3 = {15,23,43,56}

usuarios4 = {13,23,56,42}

print(usuarios3 | usuarios4)

print(usuarios3 & usuarios4)

print(usuarios3 - usuarios4)

print(usuarios3 ^ usuarios4)

usarios_geral = {1,12,13,4,56,67,8}
print(usarios_geral)
usarios_geral.add(16)
print(usarios_geral)

usarios_geral_Congelado = frozenset(usarios_geral)

meu_texto = "Alann Batista Cardoso Silva Silva".split()

print(set(meu_texto))

print(Counter(meu_texto))

aparicoes = Counter(meu_texto)

print(aparicoes["Silva"])

print(aparicoes.get("xpto",0))

aparicoes["da"] = 1

print(aparicoes)

del aparicoes["da"]

print(aparicoes)

print("Alann" in aparicoes)

print("da" in aparicoes)

for i in aparicoes.keys():
    print(i)

for i in aparicoes.values():
    print(i)

for key,value in aparicoes.items():
    print(key,value)

meu_texto = "Alann Batista Cardoso Silva Silva".lower().split()

print(meu_texto)

print(Counter(meu_texto))

aparicoes = defaultdict(int)

for palavra in meu_texto:
    aparicoes[palavra] += 1

print(aparicoes)

class Conta():
    def __init__(self):
        print("Criando Conta ....")

contas = defaultdict(Conta)

print(contas[12])
print(contas[14])
print(contas[12])


print(Counter(meu_texto))




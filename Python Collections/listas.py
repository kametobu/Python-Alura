def Tamanho_Lista(lista=None):
    if lista == None:
        lista = list()
    print(len(lista))

idades = [10,14,24,21,35]

idades.append(11)
print(idades)
idades.append(11)
print(idades)
idades.remove(11)
idades.insert(0, 9)
idades.sort()
print(idades)

idades.extend([5,12])
print(idades)
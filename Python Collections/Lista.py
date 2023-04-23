idades = [12,24,32,12,67]

for i in range(0,len(idades)):
    print(i,idades[i])

for indice, idade in enumerate(idades):
    print(indice, idade)

print(list(enumerate(idades)))


print(sorted(idades,reverse=True))
print(list(reversed(idades)))



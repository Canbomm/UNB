n = int(input())
lista = []

while n > 0:
    n -= 1
    num = int(input())
    lista.append(num)
# organizando a lista
lista.sort()

for i in range(0,len(lista)):
    if (lista[i]) % 2 == 0:
        # numero par
        print(int(lista[i]))
# organizando a lista em ordem decrescente
lista.sort(reverse=True)

for i in range(0,len(lista)):
    if (lista[i]) % 2 != 0:
        # numero impar
        print(int(lista[i]))

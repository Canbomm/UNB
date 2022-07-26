quantas_notas = int(input())
notas = []
for _ in range(quantas_notas):
    nota = float(input())
    notas.append(nota)

# na saida ele quer (nessa ordem):
# pior nota
# mediana
# melhor nota
def organizador(lista):
    tamanho = len(lista)
    if tamanho == 2:
        num1 = lista[0]
        num2 = lista[1]
        if num1 >= num2:
            return lista
        else:
            return [num2,num1]
    else:
        meio = tamanho//2 
        lista1 = organizador(lista[:meio+1])
        lista2 = organizador(lista[meio:])
        print(lista1)
        print(lista2)
        print()

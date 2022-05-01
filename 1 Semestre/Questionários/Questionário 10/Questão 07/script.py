nome_arq = input()

with open(nome_arq) as arquivo:
    lido = []
    for linha in arquivo:
        lido.append(linha.rstrip())

k = lido[0]
vetor = lido[1]

menor = vetor.min()
maior = vetor.max()

bonitoPedro1 = 0
bonitoPedro2 = 0

if maior >= (len(vetor)*2):
    bonitoPedro1 += 1


nome_arq = input()

with open(nome_arq) as arquivo:
    lido = []
    for linha in arquivo:
        lido.append(linha.rstrip())

for linha in lido:
    print(linha)

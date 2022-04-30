nome_arq = input()

with open(nome_arq) as arquivo:
    lido = []
    for linha in arquivo:
        lido.append(linha)
    for i in range(0,len(lido)-1):
        lido[i] = lido[i][:-1]

for codigo in lido:
    index = 0
    resposta = ""
    for caractere in codigo:
        print(caractere)
        try:
            print(f"Entrei no try")
            vezes = int(caractere)
            resposta += codigo[index-1]*vezes
            print(f"Entrei no try e fiz a operação")
        except:
            print(f"Entrei no except")
            resposta += caractere
        print(f"\n")
        index += 1
    print(resposta)

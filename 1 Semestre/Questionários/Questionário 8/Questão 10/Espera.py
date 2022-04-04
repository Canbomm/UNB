def contaespaco(lista):
    conta = 0
    resposta = 0
    for i in range(0,len(lista)):
        if lista[i] == 0:
            conta += 1
        else:
            if conta > resposta:
                resposta = conta
            conta = 0
    if resposta == 2:
        # por conta que ela vai sentar em um banco e vai ter alguem do lado dela
        resposta = 1
    return resposta

matriz = []
linhas,colunas = map(int,input().split())
linhas_m = linhas

while linhas_m > 0:
    matriz.append([int(x) for x in input().split()])
    linhas_m -= 1

maior = 0
for i in range(0,len(matriz)):
    espacos_fileira = contaespaco(matriz[i])
    if maior <= espacos_fileira:
        maior = espacos_fileira 

print(maior)

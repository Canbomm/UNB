def interpretaAPC(lista):
    resp = 0
    conta = -1
    for e in lista:
        resp += (e * 2**(conta))
        conta -= 1
    return resp

def codificaAPC(num,comeco):
    # eu nao sei codificar isso
    pass

comp1, comp2 = map(int,input().split())
padraoapc1 = [int(x) for x in input().split()]
padraoapc2 = [int(x) for x in input().split()]

# decodificando
apc1_dec = interpretaAPC(padraoapc1)
apc2_dec = interpretaAPC(padraoapc2)
soma_num = apc1_dec + apc2_dec
print(f"O número é: {soma_num}")

# codificando
# ???
import random

quantos = int(input("Quantas dezenas de caracteres vc deseja?\n"))*10

letras = {0:"O",1:"K",2:"D",3:"S",4:"A"}
resposta = ["inutil"]
for index in range(quantos):
    aleatorio = random.randint(0,4)
    if letras[aleatorio] != resposta[index]:
        resposta.append(letras[aleatorio])
    else:
        aleatorio2 = aleatorio
        while aleatorio2 == aleatorio:
            aleatorio2 = random.randint(0,4)
        resposta.append(letras[aleatorio2])

print("".join(resposta[1:]))

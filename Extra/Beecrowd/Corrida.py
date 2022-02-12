#entrada

#pista = int(input("Qual é o comprimento da pista em metros?\n"))
#treino = int(input("Quantos metros você pretende correr?\n"))

pista,treino = map(int,input("Qual é o comprimento da pista em metros? E quantos metros você pretende correr? (coloque apenas os valores númericos)\n").split())

#computacao
resposta = treino % pista

#saida
print(f"Deixe sua garrafa em {resposta} metro(s)")

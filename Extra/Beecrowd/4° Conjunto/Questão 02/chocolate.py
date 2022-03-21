total_de_divisoes = int(input())
divisao = map(int,input().split())
total_de_chocolate = 0

for numero in divisao:
    total_de_chocolate += numero

chocolate_guardado = total_de_chocolate - total_de_divisoes
print(chocolate_guardado)

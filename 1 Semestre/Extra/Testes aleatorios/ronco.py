import random

quantos = int(input("Quantos 'Z' vc deseja?\n"))

zzz = {0:"Z",1:"z"}
ronco = []
for _ in range(quantos):
    maiusculo = random.randint(0,1)
    ronco.append(zzz[maiusculo])

print("".join(ronco))

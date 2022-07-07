brinquedos = ["A","B","C"]
brinquedos_final = ["A","Z","C"]

soma = 0
for i in range(len(brinquedos)):
    if brinquedos[i] != brinquedos_final[i]:
        soma += 1
print(soma)

soma = 0
for i,val in enumerate(brinquedos):
    if val != brinquedos_final[i]:
        soma += 1
print(soma)
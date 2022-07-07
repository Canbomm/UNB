brinquedos = ["A","B","C"]
brinquedos_final = ["A","B","C"]
soma = 0
vezes = 0

for brinq1 in brinquedos:
    vezes += 1
    print(f"O brinquedo 1 é: {brinq1}.",f"Quantas vezes eu rodei: {vezes}")
    for brinq2 in brinquedos_final:
        print(f"O brinquedo 2 é: {brinq2}.",f"Quantas vezes eu rodei: {vezes}\n")
        if brinq1 != brinq2:
            soma += 1
        break

print(soma)
# não deu certo
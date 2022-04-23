colegasCelular = {}

for _ in range(4):
    nome = input()
    colegasCelular[nome] = (input(),int(input()))

print(f"\n\n--------========= Divisão =========-------------\n\n")
print(colegasCelular)

aparece = {}
for chave in colegasCelular:
    celular,numero = colegasCelular[chave]
    if aparece.get(celular) != None:
        aparece[celular] += 1
    else:
        aparece[celular] = 1

print(aparece)
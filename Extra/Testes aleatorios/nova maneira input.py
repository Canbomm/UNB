coisa1, coisa2 = input("Digite duas 'coisas' separadas por espaço: ").split()

print(f"A primeira coisa que você digitou foi: {coisa1}")
print(f"A segunda coisa que você digitou foi: {coisa2}")

coisa3,coisa4 = [int(x) for x in input("Digite dois números separados por espaço: ").split()]

print(f"Seu primeiro número +10 deu: {coisa3+10}")
print(f"Seu segundo número +5 deu: {coisa4+5}")

coisa5,coisa6 = ["Primeira palavra","Segunda palavra"]

print(f"Elemento 1 da lista: {coisa5}")
print(f"Elemento dois da lista: {coisa6}")

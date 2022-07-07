print("0.5")

def divisao(a):
    operacao = a - 0.25
    resultado = operacao/3.50
    print(resultado)
    if operacao > 0:
        return divisao(operacao)
    else:
        return 0
# atualizei e agora usa recursividade :emoji_de_oculos_escuros:

primeiro = divisao(1.75)

# pegar o valor do console e somar na mão mesmo
resultado = 0.5 + 0.42857142857142855 + 0.35714285714285715 + 0.2857142857142857 + 0.21428571428571427 + 0.14285714285714285 + 0.07142857142857142

print(f"A soma de tudo é: {resultado}")

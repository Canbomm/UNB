# for para contagems
# range(inicio,fim,passo). Obs: a função range usa esse intervalo "[num1,num2)", ou seja o num1 está definido e o num2 não
for num in range(1,11,1):
    print(num)

# for para input
a,b,c,d = (int(x) for x in input("Digite quatro números:\n").split())
print(f"A soma dos quatro números é {a+b+c+d}")

# for para inputs infinitos
resultado = 0
for x in input("Digite quantos números você quiser:\n").split():
    x = int(x)
    resultado += x
print(f"A soma de tudo deu {resultado}")

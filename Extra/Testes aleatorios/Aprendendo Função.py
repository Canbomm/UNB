def func1(x,y):
    print(f"Soma dos valores: {x+y}")
    print(f"Subtração dos valores: {x-y}")
    print(f"Divisão dos valores: {x/y}")
    print(f"Multiplicação dos valores: {x*y}")
    print(f"Exponenciação dos valores: {x**y}")

valor1,valor2 = map(int,input(f"Dê dois valores\n").split())
calculo = func1(valor1,valor2)

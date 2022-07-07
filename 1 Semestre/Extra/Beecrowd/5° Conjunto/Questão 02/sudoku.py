n = int(input())
total_linhas = n * 9
matriz = []

# lendo a matriz
while total_linhas > 0:
    total_linhas -= 1
    linha = [int(x) for x in input().split(" ")]
    matriz += [linha]

# peguei o input mas vou terminar de resolver outro dia
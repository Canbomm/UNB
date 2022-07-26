total_pecas = int(input())
pecas = input().split()
duplicatas = 0

while total_pecas > 0:
    peca = pecas.pop()
    if peca in pecas:
        duplicatas += 1
    total_pecas -= 1

print(duplicatas)

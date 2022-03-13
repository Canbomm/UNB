# quantos tamanhos de pipas diferentes serão feitos
pipas = int(input())

while pipas > 0:
    pipas -= 1
    pedaco1,pedaco2 = map(float,input().split())
    # area do losango formado pela cruz de bambu:
    area = (pedaco1 * pedaco2)/2
    # beecrowd não reconheceu quando eu fiz "area:.0f"
    print(f"{int(area)} cm2")

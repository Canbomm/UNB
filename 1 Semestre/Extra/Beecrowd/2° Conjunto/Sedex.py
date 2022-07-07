    #Entrada
#bb de bola de boliche
diametrobb = float(input())
#c de caixa
alturac,largurac,profundidadec = map(float,input().split(" "))

   #Computacao/Saida
if diametrobb <= alturac and diametrobb <= largurac and diametrobb <= profundidadec:
    print("S")
else:
    print("N")

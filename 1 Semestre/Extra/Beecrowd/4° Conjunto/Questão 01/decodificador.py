repeticao = int(input())
decodifica = ""

while repeticao > 0:
    repeticao -= 1
    palavra_original = input()
    for letra in palavra_original:
        letraASCII = ord(letra)
        if letraASCII >= 97 and letraASCII <= 122:
            decodifica = decodifica + letra
    print(decodifica[::-1])
    decodifica = ""

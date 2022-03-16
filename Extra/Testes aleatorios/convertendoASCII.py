palavra = input("Digite uma palavra que deseja converter pra ASCII:\n")

soma = ""
for i in palavra:
    letra = str(ord(i))+","
    soma += letra

quantosA = palavra.count("a")

print(f"\nSua palavra em ASCII:\n{soma[:-1]}\n\nPor curiosidade, sua palavra teve {quantosA} vogais 'a'")

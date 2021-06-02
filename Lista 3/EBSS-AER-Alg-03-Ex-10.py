nome_posicao = input("Me dê a posição da peça: ").lower()
casa = nome_posicao[0]
numero = int(nome_posicao[1])

if casa == "a" or casa == "c" or casa == "e" or casa == "g":
    if numero%2 ==0:
        print("A peça esta na casa branca.")
    else:
        print("A peça esta na casa preta.")

elif casa == "b" or casa == "d" or casa == "f" or casa == "h":
    if numero%2 ==0:
        print("A peça esta na casa preta.")
    else:
        print("A peça esta na casa branca.")

else:
    print("Não consegui encontrar a posição pedida.")
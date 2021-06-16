mensagem = input("Insira a mensagem que deseja codificar: ")
variante = int(input("Insira quantas posições a deslocar: "))
mensagemNova = ""
for i in mensagem:
    if ord(i) >= 65 and ord(i) <= 90:
        novoi = ord(i) + variante
        if novoi < 65:
            novoi += 90 - 64
        elif novoi > 90:
            novoi += -90 + 64
    elif ord(i) >= 97 and ord(i) <= 122:
        novoi  = ord(i) + variante
        if novoi < 97:
            novoi += 122 - 96
        elif novoi > 122:
            novoi += -122 + 96
    else:
        novoi = ord(i)
    mensagemNova += chr(novoi)

print(mensagemNova)
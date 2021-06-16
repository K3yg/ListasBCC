continuar = True

while continuar == True:
    bits = input("Insira uma sequencia de 8 bits (Caso queira finalizar, deixe em branco): ")
    if bits == "":
        continuar = False
    elif bits.count("0") + bits.count("1") != 8 or len(bits) > 8:
        print("A sequencia não é válida:")
    else:
        if bits.count("0") % 2 == 0:
            print("O bit de paridade deverá ser 0")
        else:
            print("O bit de paridade deverá ser 1")

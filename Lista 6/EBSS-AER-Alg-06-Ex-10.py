def formatar_lista(lista):
    formatado = ""
    for i in lista:
        print(formatado)
        if i is lista[len(lista)-2]:
            formatado = formatado + i + " e "
        elif i is lista[len(lista)-1]:
            formatado = formatado + i + "."
        else:
            formatado = formatado + i + ", "
    
    return formatado


def main():
    palavra = "aa"
    lista = []
    while palavra != "":
        palavra = str(input("Digite uma palavra"))
        if palavra != "":
            lista.append(palavra)

    print(formatar_lista(lista))

if __name__ == "__main__":
    main()
def remover_duplicata(lista):
    lista_unica = []
    for i in lista:
        if i not in lista_unica:
            lista_unica.append(i)
    return lista_unica

def main():
    palavra = "aa"
    print(palavra)
    lista = []
    while palavra != "":
        palavra = str(input("Digite uma palavra"))
        if palavra != "":
            lista.append(palavra)

    print(remover_duplicata(lista))

if __name__ == "__main__":
    main()
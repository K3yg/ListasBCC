def org_cresc(lista):
    lista.sort()
    return lista


def main():
    lista = []
    numero = 1
    while numero != 0:
        numero = int(input("Digite um inteiro"))
        if numero != 0:
            lista.append(numero)
            print(lista)
    print(org_cresc(lista))
    
if __name__ == "__main__":
    main()
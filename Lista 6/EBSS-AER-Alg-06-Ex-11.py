from random import randint

def remover_duplicata(lista):
    lista_unica = []
    for i in lista:
        if i not in lista_unica:
            lista_unica.append(i)
    return lista_unica


def sortear_numeros():
    lista = []
    while len(lista)<6:
        lista.append(randint(1,60))
        remover_duplicata(lista)
    lista.sort()
    return lista


def main():
    print(sortear_numeros())

if __name__ == "__main__":
    main()
def remover_extremos(lista, n):
    lista.sort()
    del lista[0:n]
    lista.sort(reverse=True)
    del lista[0:n]
    lista.sort()
    return lista

def main():
    lista = []
    numero = 1
    while numero != -1:
        numero = int(input("Digite um inteiro: -1 para sair"))
        if numero != -1:
            lista.append(numero)
            print(lista)
    n = int(input("Digite os extremos a serem removidos"))
    if len(lista) < 4:
        print("Erro")
        
    else:
        print(lista)
        print(remover_extremos(lista,n))
        

if __name__ == "__main__":
    main()
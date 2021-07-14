def countRange(lista,vmin,vmax):
    contador = 0
    for i in lista:
        item = lista[i-1]
        print(item)
        if item >= vmin:
            contador = contador + 1
            print("Contar:", contador)    
    return contador

def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    vmin = int(input("Digite o valor minimo"))
    vmax = int(input("DIgite o valor maximo"))
    print(countRange(lista,vmin,vmax))

if __name__ == "__main__":
    main()
def receber_palavras(texto):
    simbolos = [" ","?",",",".","!"]
    lista = []
    for i in range(0,len(texto)):
        if texto[i] in simbolos:
            lista.append(i)
    print(lista)


    a = texto
    for j in lista:
        print(j)
        #texto.replace(texto[j],"##")
        a = a[:j] + "#" + a[j+1:]
    print(a)
    
    final = a.split("#")
    while "" in final:
        final.remove("")
    return(final)


def main():
    texto = str(input("Digite uma frase"))
    
    print(receber_palavras(texto))
    
if __name__ == "__main__":
    main()
    
    
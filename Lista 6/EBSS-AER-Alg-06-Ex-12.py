def verificar_organizado(lista):
    if(lista == sorted(lista)):
        return True
    if(lista == sorted(lista, reverse=True)):
        return True
    return False



def main():
    numero = "a"
    lista = []
    while numero != "":
        numero = str(input("Digite um numero"))
        
        if numero != "":
            lista.append(int(numero))
            
    print(verificar_organizado(lista))
    
if __name__ == "__main__":
    main()
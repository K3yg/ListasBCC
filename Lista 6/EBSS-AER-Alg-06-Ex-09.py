def verificar_media(lista):
    resultado = []
    acima = []
    mediano = []
    abaixo = []
    media = sum(lista)/ len(lista)
    
    for i in lista:
        if i < media:
            abaixo.append(i)
        if i == media:
            mediano.append(i)
        if i > media:
            acima.append(i)
            
    resultado = [abaixo,mediano,acima]
    
    return resultado

def main():
    numero = "a"
    lista = []
    while numero != "":
        numero = str(input("Digite um numero"))
        
        if numero != "":
            lista.append(int(numero))
    
    resultado = verificar_media(lista)
    print("Abaixo: ", resultado[0])
    print("Média: ", resultado[1] )
    print("Acima: ", resultado[2])
    

if __name__ == "__main__":
    main()
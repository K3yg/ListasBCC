def organizar_numeros(lista):
    resultado = []
    for i in lista:
        if i < 0:
            resultado.append(i)
    for i in lista:
        if i == 0:
            resultado.append(i)
    for i in lista:
        if i > 0:
            resultado.append(i)
    
    return resultado

def main():
    numero = "a"
    lista = []
    while numero != "":
        numero = str(input("Digite um numero"))
        
        if numero != "":
            lista.append(int(numero))
            
    for i in range(len(lista)):
        print(organizar_numeros(lista)[i])
    

if __name__ == "__main__":
    main()
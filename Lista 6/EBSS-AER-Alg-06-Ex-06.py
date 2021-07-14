def listar_divisores(numero):
    resultado = []
    for i in range (1,numero):
        if numero%i == 0:
            resultado.append(i)
    return resultado


def main():
    numero = int(input("Digite um inteiro"))
    print(listar_divisores(numero))
    
if __name__ == "__main__":
    main()
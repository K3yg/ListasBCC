def calcular_mediana(numero1,numero2,numero3):
    lista = [numero1,numero2,numero3]
    lista = sorted(lista)
    return lista[1]


def main():
    numero1 = float(input("Digite um numero"))
    numero2 = float(input("Digite um numero"))
    numero3 = float(input("Digite um numero"))
    print(calcular_mediana(numero1,numero2,numero3))
    
if __name__ == "__main__":
    main()
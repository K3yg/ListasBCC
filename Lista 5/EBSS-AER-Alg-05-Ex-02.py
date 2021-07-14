def calcular_tarifa(distancia):
    a=4
    b=0.25
    tarifa = a + (((distancia*1000)//140)*b)
    return tarifa



def main():
    distancia = float(input("Digite a distancia percorrida em km"))
    print(calcular_tarifa(distancia))
    

if __name__ == "__main__":
    main()
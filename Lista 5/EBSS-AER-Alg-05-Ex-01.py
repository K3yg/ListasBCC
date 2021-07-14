from math import sqrt

def calcular_pitagora(ladoa,ladob):
    hipotenusa = sqrt((ladoa**2)+(ladob**2))
    return hipotenusa



def main():
    ladoa = float(input("Digite o lado a"))
    ladob = float(input("Digite o lado b"))
    print(calcular_pitagora(ladoa,ladob))

if __name__ == "__main__":
    main()
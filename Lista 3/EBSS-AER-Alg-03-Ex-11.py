import math


a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raizes reais.")

elif delta == 0:
    bhaskara = ((b)*-1 + math.sqrt(delta))/(2*a)
    print(f'A equação possui apenas uma raiz real: {bhaskara}.')

else:
    bhaskarapositivo = ((b)*-1 + math.sqrt(delta))/(2*a)
    bhaskaranegativo = ((b)*-1 - math.sqrt(delta))/(2*a)
    print(f'A equação possui duas raizes: {bhaskarapositivo} e {bhaskaranegativo}')
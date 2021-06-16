x = int(input("Insira um valor para radiciar: "))
raiz = x
while abs(x - raiz * raiz)  > (10 ** (-12)):
    print(raiz)
    raiz = (raiz + (x / raiz)) / 2
    
print("A raíz é:", raiz)


    
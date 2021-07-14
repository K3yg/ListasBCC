def int2hex(dec):
    letras = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letras[int(dec)]

def hex2int(hex):
    letras = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return int(letras.find(hex.upper()))

def converter_paradec(num,base):
    numf = 0
    contador = len(str(num))*-1
    while contador < 0:
        numf += int(hex2int(num[contador])  *  (   int(base)**(  (int(contador)*-1) -1) ) )
        contador = contador+1
    return numf
        
def decparabase(num,base):
    numf = ""
    while int(num)>=int(base):
        numf = numf + str(int2hex(int(num)%int(base)))
        num = int(num)//int(base)
    numf = numf +str(int2hex(num))
    return str(numf)[::-1]


def main():
    num = input("Digite o numero")
    base = input("Digite a base do numero")
    basef = input("Digite a base de destino")
    convertido = converter_paradec(num,base)
    final = decparabase(convertido,basef)
    print(final)

if __name__ == "__main__":
    main()
def int2hex(dec):
    #letras = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
    letras = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letras[int(dec)]

def hex2int(hex):
    
    letras = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letras.find(hex.upper())

def main():
    x = input("Digite um numero HEXADECIMAL")
    print(hex2int(x))
    x = input("Digite um numero DECIMAL")
    print(int2hex(x))
    
if __name__ == "__main__":
    main()
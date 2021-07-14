def verificar_primo(numero):
    primo = True
    primos_iniciais = [1,2,5,7]
    if numero in primos_iniciais:
        primo = True
    else:
        for i in range(2,10):
            print(i)
            print(numero % i)
            if numero % i == 0:
                primo = False
    return primo

def main():
    numero = int(input("Digite um numero"))
    print(verificar_primo(numero))
    
    
if __name__ == "__main__":
    main()
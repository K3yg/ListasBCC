def verificar_perfeito(numero):
    resultado = []
    for i in range (1,numero):
        if numero%i == 0:
            resultado.append(i)
    soma = sum(resultado)
    
    if soma == numero:
        return True


def main():
    for i in range(1,10001):
        if verificar_perfeito(i):
            print(i)
    
if __name__ == "__main__":
    main()
'''MDC - Máximo Divisor Comum. Euclides foi um matemático grego que viveu há
aproximadamente 2.300 anos. Seu algoritmo para calcular o MDC - máximo divisor comum de
dois inteiros positivos, a e b, é eficiente e recursivo. Está descrito abaixo:

Escreva um programa que implemente o algoritmo recursivo de Euclides e o use para
determinar o máximo divisor comum de dois inteiros inseridos pelo usuário.'''


def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


def main ():
    a = int(input("Digite um número inteiro positivo: "))
    b = int(input("Digite outro número inteiro positivo: "))
    print("O máximo divisor comum entre", a, "e", b, "é: ", mdc(a, b))

if __name__ == '__main__':
    main()
'''Fatorial. Implementa uma função recursiva para calcular o fatorial de um número inteiro
positivo. O fatorial é denotado pelo símbolo de exclamação “!” e é definido da seguinte forma:
1! = 1 e n! = n x (n-1)!, para n>1.'''


def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def main():
    n = int(input("Digite um número inteiro positivo: "))

    print(fatorial(n))


if __name__ == '__main__':
    main()
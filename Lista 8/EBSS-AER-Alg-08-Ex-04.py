'''Fibonacci com memorização de resultado. Escreva uma nova versão da sua função
recursiva do exercício 2 (Fibonacci) utilizando a técnica de memorização de resultado para
melhorar desempenho e consumo de memória.'''

resultados_conhecidos = {0: 0, 1: 1}

def fibonacci(n):
    if n in resultados_conhecidos:
        return resultados_conhecidos[n]
    resposta = fibonacci(n-1) + fibonacci(n-2)
    resultados_conhecidos[n] = resposta
    return resposta

def main():
    n = int(input("Digite um número inteiro: "))
    print(fibonacci(n))

if __name__ == '__main__':
    main()



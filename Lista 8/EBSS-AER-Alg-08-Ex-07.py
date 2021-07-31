'''Conversão decimal → binário iterativa. Escreva uma função que converte um número
decimal (base 10) em binário (base 2). A função deve receber como parâmetro o número
inteiro decimal (q) e, em seguida, deve realizar a conversão usando o algoritmo de divisão
mostrado abaixo. Quando o algoritmo for concluído, o resultado contém a representação
binária do número, que deve ser retornada pela função como uma string.'''

def decimalTobin(q,result = ""):
    while q!=0:
        r = q%2
        result = str(r) + result
        q = q//2
    return (result)

def main():
    print("Conversão decimal → binário iterativo")
    x = int(input("Digite um número inteiro: "))
    print(decimalTobin(x))

if __name__ == "__main__":
    main()
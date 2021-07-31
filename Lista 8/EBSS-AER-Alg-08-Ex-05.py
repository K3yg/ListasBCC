'''Total de valores numéricos. Escreva um programa que leia os valores numéricos do usuário
até que uma linha em branco seja inserida. Exiba a soma total de valores inseridos pelo
usuário (ou 0,0 se o primeiro valor inserido for uma linha em branco). Conclua esta tarefa
usando recursão. Seu programa não pode usar nenhum laço de repetição.'''

def valor_numerico():
    valor = input('Digite um valor inteiro: ')
    if valor == '':
        return 0
    else:
        return int(valor + valor_numerico())

print(valor_numerico())

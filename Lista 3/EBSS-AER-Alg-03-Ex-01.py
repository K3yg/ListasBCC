'''
Par ou ímpar. Escreva um programa Python que recebe do usuário um número inteiro. Seu
programa deve então exibir uma mensagem indicando se o número fornecido é par ou ímpar.
'''


x = int(input('Digite um número inteiro: '))

if x%2 == 0:
    print(f'{x} é par!')
elif x%2 != 0:
    print(f'{x} é ímpar!')
else:
    print('Insira um numero válido, por favor.')



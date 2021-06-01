'''
Níveis de barulho. A tabela abaixo mostra uma lista de volume sonoro em decibéis para
diferentes tipos comuns de barulhos.

Escreva um programa Python que receba do usuário um nível de volume em decibéis. Se o
usuário entrar com um valor igual a um daqueles listados na tabela, então seu programa deve
exibir uma mensagem informando o tipo de barulho da tabela equivalente ao valor informado.
Se o usuário entrar um valor intermediário entre dois valores da tabela, então seu programa
deve exibir uma mensagem informando que o nível está entre os dois barulhos (deve informar
quais são eles). Certifique-se também que seu programa exiba mensagens apropriadas caso o
usuário entre com valor menor que o menor valor da tabela ou maior que o maior valor.

'''

db = float(input('Inisira o nível de decibéis: '))

sil = float(40)
desp =float (70) 
cort = float(106)
brit = float(130)

if db == sil:
    print('O nível de dB é de uma sala silenciosa!')
elif db == desp:
    print('O nível de dB é de um despertador!')
elif db == cort:
    print('O nível de dB é de um cortador de grama!')
elif db == brit:
    print('O nível de dB é de uma britadeira!')
elif db > sil and db < desp:
    print('O nível de dB está entre uma sala silenciosa e um despertador!')
elif db > desp and db < cort:
    print('O nível de dB está entre um despertador e um cortador de grama!')
elif db > cort and db < brit:
    print('O nível de dB está entre um cortador de grama e uma britadeira!')
elif db > brit:
    print('O nível de dB está acima de uma britadeira!')
elif db < sil:
    print('O nível de dB está abaixo de uma sala silenciosa!')
else:
    print('Insira um valor válido!')
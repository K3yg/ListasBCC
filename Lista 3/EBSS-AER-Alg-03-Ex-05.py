'''
Nome do mês e número de dias. A quantidade de dias de um m6es pode variar de 28 a 31
dias. Neste exercício você deve criar um programa Python que recebe do usuário o nome de um mês (como uma string). Então seu programa deve exibir uma mensagem informando a
quantidade de dias daquele mês. Caso o mês seja fevereiro, sua mensagem pode informar
“28 ou 29 dias”.
'''

mes = str.lower(input('Digite o nome do mês: '))

if mes == 'janeiro':
    print(f'{str.capitalize(mes)} tem 31 dias.')
elif mes == 'fevereiro':
    print(f'{str.capitalize(mes)} tem 28 ou 29 dias.')
elif mes == 'março':
    print(f'{str.capitalize(mes)} tem 31 dias.')
elif mes == 'abril':
    print(f'{str.capitalize(mes)} tem 30 dias.')
elif mes == 'maio':
    print(f'{str.capitalize(mes)} tem 31 dias.')
elif mes == 'junho':
    print(f'{str.capitalize(mes)} tem 30 dias.')
elif mes == 'julho':
    print(f'{str.capitalize(mes)} tem 31 dias.')
elif mes == 'agosto':
    print(f'{str.capitalize(mes)} tem 31 dias.')
elif mes == 'setembro':
    print(f'{str.capitalize(mes)} tem 30 dias.')
elif mes == 'outubro':
    print(f'{str.capitalize(mes)} tem 31 dias.')
elif mes == 'novembro':
    print(f'{str.capitalize(mes)} tem 30 dias.')
elif mes == 'dezembro':
    print(f'{str.capitalize(mes)} tem 31 dias.')
else:
    print('Digite um mês válido!')
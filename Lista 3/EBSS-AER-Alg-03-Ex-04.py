'''
Polígono regular. Crie um programa Python que determina e exibe o nome de um polígono
regular sendo fornecida pelo usuário a quantidade de lados. Seu programa deve suportar
polígonos de 3 a 10 lados (inclusive). Caso o usuário forneça valores fora desta faixa, o
programa deve exibir uma mensagem de erro.
'''

qnt_lados = int(input('Insira a quantidade de lados: '))

if qnt_lados == 3:
    print('Seu polígono é um triangulo')
elif qnt_lados == 4:
    print('Seu poligono é um quadrado')
elif qnt_lados == 5:
    print('Seu polígono é um pentágono')
elif qnt_lados == 6:
    print('Seu polígono é um hexágono')
elif qnt_lados == 7:
    print('Seu poligono é um heptágono')
elif qnt_lados == 8:
    print('Seu poligono é um octógono')
elif qnt_lados == 9:
    print('Seu poligono é um eneágono')
elif qnt_lados == 10:
    print('Seu poligono é um decágono')
else:
    print('Insira uma quantidade de lados válida')


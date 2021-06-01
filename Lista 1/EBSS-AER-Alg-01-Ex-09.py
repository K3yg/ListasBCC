

#ler valor inicial depositado
capital = int(input('Insira o valor depositado: '))

#calcular o montante
taxajuros = 12
tempo = 1

for r in range(3):
    m = capital * (1+(taxajuros/100))**tempo
    print(f'Valor total obtido após {tempo} ano(s): {m:.2f}')
    tempo = tempo + 1
    



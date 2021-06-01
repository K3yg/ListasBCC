'''
Classifique o triângulo. Baseado nos comprimentos dos seus lados, um triângulo pode ser
classificado como equilátero (quando os três lados tem o mesmo tamanho), isósceles (quando
apenas dois lados são iguais) ou escaleno (quando os três lados são diferentes). Escreva um
programa Python que recebe do usuário os comprimentos dos 3 lados de um triângulo e exiba
uma mensagem informando qual é o tipo do triângulo.
'''

lado_1 = float(input('Insira o comprimento de um lado: '))
lado_2 = float(input('Insira o comprimento de outro lado: '))
lado_3 = float(input('Insira o comprimento de mais um lado: '))


if lado_1 == lado_2 and lado_2 == lado_3:
    print('Seu triângulo é equilátero')

elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print('Seu triângulo é isósceles')

elif lado_1 != lado_2 != lado_3:
    print('Seu triângulo é escaleno')
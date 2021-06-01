'''
Área de um polígono regular. Um polígono é regular se seus lados são todos do mesmo
tamanho e os ângulos entre lados adjacentes são todos iguais. A área de um polígono regular
pode ser calculada pela fórmula abaixo onde l é o comprimento de um lado e n é o número de
lados:

Escreva um programa Python que obtenha do usuário os valores de l e n, e então calcule e
exiba a área do polígono regular correspondente.

'''

import math


l = float(input('Insira o comprimento do lado: '))
n = float(input('Insira o número de lados: '))

area = (n*(l**2)) / 4 * (math.tan *(math.pi/n))

print(area)
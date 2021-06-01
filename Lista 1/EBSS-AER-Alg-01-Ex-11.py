'''
A terra é curva (a não ser para os terraplanistas! ) e
a distância entre graus de longitude (leste-oeste) varia conforme a latitude (norte-sul). Com
isso, encontrar a distância entre dois pontos na superfície da terra é mais complicado do
simplesmente usar o Teorema de Pitágoras no plano. Seja e as latitudes e
longitudes de dois pontos na superfície da terra. A distância em quilômetros entre estes dois
pontos ao longo da superfície da terra é dada por:

distancia = 6371.01 × arccos(sen(t1) × sen(t2) + cos(t1) × cos(t2) × cos(g1 − g2))

Crie um programa Python que receba a latitude e a longitude de dois pontos na Terra em
graus, calcule e exiba a distância entre eles em quilômetros ao longo da superfície.

as funções trigonométricas do Python operam em radianos (e não em graus).
Com isso, você vai precisar converter os dados de graus para radianos antes de calcular a
distância. O módulo matemático do Python contém uma função chamada radianos, que faz
esta conversão.

'''
from math import acos, radians, cos, sin, asin, sqrt

g1 = float(input('Insira a longitude do primeiro local: '))
t1 = float(input('Insira a latitude do segundo local: '))
g2 = float(input('Insira a longitude do primeiro local: '))
t2 = float(input('Insira a latitude do segundo local: '))


g1, t1, g2, t2 = map(radians, [g1, t1, g2, t2])


dist = 6371.01 * acos(  (sin(t1)) * (sin(t2)) * (cos(t1)) * (cos(t2)) * (cos(g1 - g2))    )

print(str(round(dist,2)) + " km" )
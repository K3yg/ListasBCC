import math

l1 = float(input('Insira o comprimento do lado 1: '))
l2 = float(input('Insira o comprimento do lado 2: '))
l3 = float(input('Insira o comprimento do lado 3: '))

l = (l1 + l2 + l3)/2

area = math.sqrt(l*(l-l1)*(l-l2)*(l-l3))

print(area)
from math import sqrt

run = True
first = True
d = 0

while run == True:
    if first == True:
        x1 = input("Insira a coordenada x de um ponto: ")
        y1 = input("Insira a coordenada y de um ponto: ")
        x = x1
        y = y1
        first = False
    else:
        temp = input("Insira a coordenada x de um ponto (enter para sair): ")
        if temp != "":
            x1 = temp
            y1 = input("Insira a coordenada y de um ponto: ")
            d += sqrt(abs(float(y2) - float(y1)) ** 2 + abs(float(x2) - float(x1)) ** 2)
        
        else:
            d += sqrt(abs(float(y) - float(y1)) ** 2 + abs(float(x) - float(x1)) ** 2)
            run = False
    x2 = x1
    y2 = y1

print(f"O perímetro deste polígono é igual a {d}")
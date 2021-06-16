pi = 3
contador = 0
for i in range(15):
    contador += 2
    if i % 2 == 0:
        pi += 4 / ((contador) * (contador+1) * (contador+2))
    else:
        pi -= 4 / ((contador) * (contador+1) * (contador+2))

print(pi)

x = True
contador = 0
acumulador = 0


while x == True:
    y = int(input("Insira um número: "))
    if y == 0:
        x = False
    else:
        acumulador += y
        contador += 1

if acumulador == 0:
    print("Erro! O primeiro número não pode ser 0")
else:
    print(f"A média é {acumulador / contador:.2f}")
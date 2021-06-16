x = int(input("Insira um número inteiro (que seja maior ou igual a 2): "))
fator = 2
while fator <= x:
    if x % fator == 0:
        print(fator)
        x //= fator
    else:
        fator += 1
        
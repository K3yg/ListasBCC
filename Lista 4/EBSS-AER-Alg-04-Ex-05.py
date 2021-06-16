continuar = True
soma = 0

while continuar == True:
    idade = input("Insira a idade de um visitante (Caso queira finalizar, deixe em branco): ")
    if idade == "":
        continuar = False
    else:
        idade = int(idade)
        if idade < 3:
            soma += 0
        elif idade <= 12:
            soma += 14
        elif idade <= 65:
            soma += 18
        else:
            soma += 23

print(f"O valor total é de R$ {soma:.2f}")
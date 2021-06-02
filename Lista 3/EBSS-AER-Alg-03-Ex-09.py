'''
Data de feriado. A tabela abaixo mostra os feriados nacionais brasileiros que caem sempre no
mesmo dia (em oposição aos feriados variáveis como carnaval e corpus christi).

Escreva um programa Python que leia do usuário o mês e o dia de uma determinada data. Se
o mês e o dia corresponderem a uma das datas da tabela acima, seu programa deve exibir o
nome do feriado. Caso contrário o programa deve informar que o dia e o mês informados não
correspondem a um feriado nacional.
'''


mes = input("Insira o mês: ").lower()
dia = int(input("Insira o dia: "))

if dia == 1:
    if mes == "janeiro":
        print("Confraternização universal")
    elif mes == "maio":
        print("Dia do trabalho")

elif mes == "abril" and dia == 21:
    print("Tiradentes")

elif mes == "setembro" and dia == 7:
    print("Independência do Brasil")

elif mes == "outubro" and dia == 12:
    print("Nossa Senhora Aparecida")

elif mes == "novembro":
    if dia == 2:
        print("Finados")
    if dia == 15:
        print("Proclamação da República")

elif mes == "dezembro" and dia ==25:
    print("Natal")

else:
    print("O dia e o mês informados não correspondem a um feriado nacional.")
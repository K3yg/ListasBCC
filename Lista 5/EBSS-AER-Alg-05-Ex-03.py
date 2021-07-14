def calcular_envio(qntd_itens):
    qntd_itens = qntd_itens - 1
    preco = 10.95 + qntd_itens*2.95
    return preco

def main():
    qntd_itens = float(input("Digite a quantidade de itens"))
    print("%.2f" %calcular_envio(qntd_itens))
    

if __name__ == "__main__":
    main()
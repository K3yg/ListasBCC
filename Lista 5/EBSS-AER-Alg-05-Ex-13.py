def verificar_bissexto(ano):
    if ano % 400 == 0:
        return True

    elif ano %100 == 0:
        return False

    elif ano %4 == 0:
        return True
        
    else:
        return False
    
def contar_dias(mes,ano):
    if mes == 2:
        if verificar_bissexto(ano):
            dias = 29
        else:
            dias = 28
        
    elif mes in [1,3,5,7,8,10,12]:
        dias = 31
    else:
        dias= 30
        
    return dias

def main():
    mes = int(input("Digite um mes: "))
    ano = int(input("Digite um ano: "))
    print(contar_dias(mes,ano))


if __name__ == "__main__":
    main()
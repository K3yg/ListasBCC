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

def verificar_datamagica(dia,mes,ano):
    if dia*mes == int(str(ano)[2:]):
        return True
    else:
        return False

def main():

    for i in range(1901,2001):
        for j in range(1,13):
            dias = contar_dias(j,i)
            for k in range (1,dias+1):
                if verificar_datamagica(k,j,i):
                    print(k,j,i)
                

if __name__ == "__main__":
    main()
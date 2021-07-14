def transformar_maiuscula(frase):
    a = ""
    sinais = [".","!","?"]
    
    for i in range(len(frase)):
        if i == 0:
            a = a + frase[i].upper()
        
        elif frase[i-2] in sinais:
            a = a + frase[i].upper()
        
        else:
            a = a+frase[i]
            
    return a

def main():
    frase = str(input("Digite uma frase"))
    print(transformar_maiuscula(frase))
    

if __name__ == "__main__":
    main()
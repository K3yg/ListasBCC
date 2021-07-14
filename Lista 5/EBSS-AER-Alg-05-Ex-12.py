def validar_senha(senha):
    numero = [0,1,2,3,4,5,6,7,8,9]
    
    if len(senha) < 9:
        return False
    if senha.upper() == senha:
        return False
    if senha.lower() == senha:
        return False
    for i in numero:
        print(str(numero[i]))
        print(senha)
        if str(numero[i]) in senha:
            return True
        else:
            valido = False
    return valido


def main():
    senha = input("Digite a senha")
    print(validar_senha(senha))
    
if __name__ == "__main__":
    main()
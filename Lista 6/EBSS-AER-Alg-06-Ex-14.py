def determinar_precedencia(operador):
    if operador == "+" or operador=="-":
        return 1
    elif operador =="*" or operador =="/":
        return 2
    elif operador =="^":
        return 3
    else:
        return -1

def main():
    operador = input("Digite o operador")
    print(determinar_precedencia(operador))

if __name__ == "__main__":
    main()
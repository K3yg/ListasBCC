def validar_triangulo(a,b,c):
    lista = [a,b,c]
    lista = sorted(lista)
    if lista[0] + lista[1] > lista[2]:
        return "Válido"
    else:
        return "Inválido"
    
    
def main():
    a = float(input("Digite o lado a"))
    b = float(input("Digite o lado b"))
    c = float(input("Digite o lado c"))
    print(validar_triangulo(a,b,c))

if __name__ == "__main__":
    main()
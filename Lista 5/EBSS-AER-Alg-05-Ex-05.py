def definir_ordinal(numero):
    if numero <= 12:
        lista_ordinal = ["primeiro","segundo","terceiro","quarto","quinto","sexto","setimo","oitavo","nono","decimo","decimo primeiro", "decimo segundo"]
        numero_ordinal = lista_ordinal[numero-1]
        return numero_ordinal
    if numero> 12:
        return ""

def main():
    numero = int(input("DIgite um numero de 1 a 12"))
    print (definir_ordinal(numero))
    
    
if __name__ == "__main__":
    main()
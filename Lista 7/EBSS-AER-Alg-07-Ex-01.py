"""Caracteres únicos. Escreva uma função Python para verificar se uma string possui
caracteres únicos. Por exemplo, a string “azul" não repete letras, mas a string
“ferramenta"possui letras repetidas. A função deve receber uma string e retornar True no
primeiro caso (letras únicas) ou False caso contrário (letras repetidas). Você deve usar
conjuntos para implementar a função."""


def verificar_caracter_unico(string):
    letras_dif = set(string)
    for caracter in letras_dif:
        letras_dif.add(caracter)
    if len(letras_dif) == len(string):
        return True
    else:
        return False
        

def main():
    palavra = input("Digite uma palavra para verificar se há repetição de caracteres nela: ")

    print(verificar_caracter_unico(palavra))

if __name__ == '__main__':
    main()
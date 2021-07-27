'''Código morse. O código morse é um esquema de codificação de letras e números utilizando
pontos e traços. Neste exercício você deve escrever um programa que usa um dicionário para
armazenar o mapeamento de letras e números para código Morse. Voce deve representar os
pontos com símbolo de ponto “.” e traços com sinal de subtração “-“. A tabela abaixo mostra o
mapeamento de letras e números para código Morse. Seu programa deve ler uma mensagem
do usuário e então deve traduzir cada letra e número para código Morse, deixando um espaço
em branco entra cada caractere traduzido. O programa deve ignorar qualquer caracter que
não seja letra ou número. Por exemplo, a mensagem Hello, World! Deve ser exibida da
seguinte forma: .... . .-.. .-.. --- .-- --- .-. .-.. -..'''

def transformar_morse(frase):
    dicionario_morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}
    morse = ""
    frasenormal = frase.upper()
    for letra in frasenormal:
        try:
            morse = morse + dicionario_morse[letra] + " "
        except:
            pass
    return morse
        
def main():
    x = input("Digite uma frase")
    print(transformar_morse(x))


if __name__ == "__main__":
    main()
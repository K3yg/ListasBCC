'''Anagramas novamente. A noção de anagramas pode ser estendida para múltiplas palavras.
Por exemplo: "William Shakespeare” e “I am a weakish speller” são anagramas se ignorarmos
se as letras são maiúsculas e também os espaços. Crie uma nova versão da sua função do
exercício anterior para verificar se duas frases são anagramas. Sua função deve
desconsiderar se as letras são maiúsculas ou minúsculas, ignorar espaços e sinais de
pontuação.'''

def verificar_anagrama(palavra1,palavra2):
    d = {}
    d2 = {}
    for i in range(len(palavra1)):
        if palavra1[i] not in d:
            d[palavra1[i]] = i
            

    for j in range(len(palavra2)):
        d2[palavra2[j]] = j
    print(d,d2)
    
    
def verificar_anagrama(palavra,palavra1):
    palavra = palavra.upper()
    palavra = palavra.replace(" ","")
    palavra1 = palavra1.upper()
    palavra1 = palavra1.replace(" ","")
    
    d = {}
    for letra in palavra:
        if letra in ["?","!",",",".",":",";"]:
            pass
        else:
            d[letra] = d.get(letra, 0) + 1
    d1 = {}
    for letra in palavra1:
        if letra in ["?","!",",",".",":",";"]:
            pass
        else:
            d1[letra] = d1.get(letra, 0) + 1
    
    print(d1,d)    
    if d == d1:
        return True
    else:
        return False

def main():
    x = input("Digite uma frase")
    y = input("Digite uma frase")
    print(verificar_anagrama(x,y))

if __name__ == "__main__":
    main()
'''Anagramas. Duas palavras são anagramas se contiverem as mesmas letras, mas em ordens
diferentes. Por exemplo: “amor" e “roma" são anagramas porque cada uma delas contém um
"a", um "o", um "m" e um “r”. Crie uma função Python que recebe duas strings e retorna True
se elas forem anagramas, ou False caso contrário.'''

def verificar_anagrama(palavra1,palavra2):
    d = {}
    d2 = {}
    for i in range(len(palavra1)):
        if palavra1[i] not in d:
            d[palavra1[i]] = i
            

    for j in range(len(palavra2)):
        d2[palavra2[j]] = j
    print(d,d2)
    
    
def verificar_anagrama(palavra,palavra2):
    palavracerta = palavra.upper()
    palavracerta1 = palavra2.upper()
    
    d = {}
    for letra in palavracerta:
        d[letra] = d.get(letra, 0) + 1
    d1 = {}
    for letra in palavracerta1:
        d1[letra] = d1.get(letra, 0) + 1
    
    
    if d == d1:
        return True
    else:
        return False

def main():
    x = input("Digite uma palavra")
    y = input("Digite uma palavra")
    print(verificar_anagrama(x,y))

if __name__ == "__main__":
    main()
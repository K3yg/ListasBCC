'''Cartela de bingo. Uma cartela de bingo é formada por 5 linhas e 5 colunas. As colunas são
rotuladas com as letras B, I, N, G e O. Existem 15 números diferentes que podem aparecer
abaixo de cada letra. Abaixo do B podem aparecer os números de 1 a 15; abaixo do I os
números de 16 a 30, abaixo do N os números de 31 a 45 e assim por diante. Escreva uma
função que cria uma cartela de bingo e a armazena em um dicionário. As chaves do dicionário
são as letras B, I, N, G e O. Os valores devem ser listas de 5 números cada, que aparecem
abaixo de cada letra na cartela. A função deve retornar o dicionário. Escreva uma segunda
função que recebe o dicionário e exibe a cartela de bingo com as colunas rotuladas
apropriadamente. Escreva um programa main que gere e exiba uma cartela de bingo usando
suas funções.'''


import random

def gerar_cartela():
    b = []
    while len(b) != 5:
        rng = random.randint(1,15)
        if rng not in b:
            b.append(rng)
            
    i = []
    while len(i) != 5:
        rng = random.randint(16,30)
        if rng not in i:
            i.append(rng)
    n = []
    while len(n) != 5:
        rng =random.randint(31,45)
        if rng not in n:
            n.append(rng)
    g = []
    while len(g) != 5:
        rng = random.randint(46,60)
        if rng not in g:
            g.append(rng)
    o = []
    while len(o) != 5:
        rng = random.randint(61,75)
        if rng not in o:
            o.append(rng)
    b.sort()
    i.sort()
    n.sort()
    g.sort()
    o.sort()
    cartela = {"B":b,"I":i,"N":n,"G":g,"O":o}
    return cartela

#def exibir_cartela(cartela):
    

def exibir_cartela(cartela):
    x = ""
    print("| B  | i  | n  | g  | o  |\n--------------------------")
    for j in range (5):
        lista = []
        for i in cartela:
            lista.append(cartela[i][j])
        if lista[0]<10:
            x = str(lista[0]) + " "
        else:
            x = lista[0]
            
            
        print("|",x,"|",lista[1],"|",lista[2],"|",lista[3],"|",lista[4],"|")
        
def main():
    cartela = gerar_cartela()
    exibir_cartela(cartela)
    

if __name__ == "__main__":
    main()
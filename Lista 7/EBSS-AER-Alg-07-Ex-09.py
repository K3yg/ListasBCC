'''Jogo de Bingo. Neste exercício você vai simular o jogo de Bingo para apenas uma cartela.
Começa gerando uma lista de todas as chamadas válidas de bingo (B1 até O75). Depois que
a lista estiver pronta, você pode embaralhar seus elementos chamando a função shuffle do
módulo random do Python. Então seu programa deve ir utilizando os valores da lista para
anunciar os números sorteados e zerar os números correspondentes na cartela até que ela
contenha uma linha, coluna ou diagonal zerada. No seu programa principal, faça uma
simulação de 1.000 partidas (sempre com uma nova cartela) e mostre o número mínimo, o
máximo e a média de chamadas até que se tenha uma cartela vencedora. Utilize seu código
dos dois exercícios anteriores e não se esqueça de criar novas funções sempre que você
identificar algum procedimento que pode ser melhor organizado dentro de uma função.'''

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
    #print(cartela)
    return cartela

#def exibir_cartela(cartela):
    

def exibir_cartela(cartela):
    novalista = []
    x = ""
    print("\n| B  | i  | n  | g  | o  |\n*----------------------------*")
    for j in range (5):
        novalista = []
        lista = []
        for i in cartela:
            lista.append(cartela[i][j])
        for cu in range(5):
            if lista[cu]<10:
                novalista.append(str(lista[cu]) + " ")
            else:
                novalista.append(lista[cu])
        print("|",novalista[0],"|",novalista[1],"|",novalista[2],"|",novalista[3],"|",novalista[4],"|")
    print("*------------------------*\n")
        
        

def verificar_vencedor(cartela):
    if cartela["B"][0] + cartela["I"][1] + cartela["N"][2] + cartela["G"][3]+ cartela["O"][4] == 0 or cartela["B"][4] + cartela["I"][3] + cartela["N"][2] + cartela["G"][1]+ cartela["O"][0] == 0:
        return True
    for j in range (5):
        lista = []
        for i in cartela:
            if sum(cartela[i]) == 0:
                return True
            lista.append(cartela[i][j])
        if sum(lista) == 0:
            return True
    
    return False
        

def jogar_bingo(cartela):
    lista_possiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
    random.shuffle(lista_possiveis)
    #lista_possiveis = [35, 70, 12, 55, 57, 22, 10, 47, 44, 56, 52, 53, 45, 65, 46, 36, 26, 67, 2, 41, 58, 39, 68, 43, 71, 62, 54, 33, 20, 19, 15, 64, 25, 40, 23, 73, 38, 32, 27, 17, 60, 34, 3, 61, 5, 8, 50, 74, 13, 42, 6, 16, 1, 49, 72, 7, 18, 63, 30, 66, 
#24, 21, 14, 51, 29, 69, 11, 9, 31, 4, 48, 75, 59, 28, 37]
    
    contador = 0
    lista = []
    for numero in lista_possiveis:
        if verificar_vencedor(cartela)==True:
            return contador
        contador += 1
        for letra in cartela:
            for i in range (0,5):
                if cartela[letra][i] == numero:
                    #print("NUMERO DA CARTELA: ", cartela[letra][i],"NUMERO SORTEADO: ",numero,"QUANTIDADE DE SORTEIOS: ",contador )
                    lista = cartela[letra]
                    lista = [0 if k==numero else k for k in lista]
                    cartela[letra] = lista
                    #exibir_cartela(cartela)

def main():
    
    #cartela = gerar_cartela()
    #cartela_vert= {"B":[19, 20, 23, 25, 30],'I': [0,0,0,0,0], 'N': [33, 35, 36, 38, 43], 'G': [47, 50, 56, 57, 60], 'O': [61, 62, 68, 70, 71]}
    #cartela_hor = {'B': [0, 8, 9, 12, 13], 'I': [0, 20, 23, 25, 30], 'N': [0, 35, 36, 38, 43], 'G': [0, 50, 56, 57, 60], 'O': [0, 62, 68, 70, 71]}
    #artela_diag = {'B': [0, 8, 9, 12, 13], 'I': [19, 0, 23, 25, 30], 'N': [33, 35, 0, 38, 43], 'G': [47, 50, 56, 0, 60], 'O': [61, 62, 68, 70, 0]}
    #cartela_perdida = {'B': [0, 0, 0, 0, 13], 'I': [0, 20, 23, 25, 30], 'N': [0, 35, 36, 38, 43], 'G': [0, 50, 56, 57, 60], 'O': [61, 62, 68, 70, 71]}
    #cartela = {'B': [5, 6, 7, 10, 0], 'I': [20, 22, 23, 0, 29], 'N': [35, 40, 0, 43, 44], 'G': [46, 0, 50, 59, 60], 'O': [0, 70, 71, 73, 75]}
    resultados = []
    for i in range (1000): 
        print(i)
        cartela = gerar_cartela()
        x = jogar_bingo(cartela)
        resultados.append(x)
        
    print(len(resultados))
    print(min(resultados))
    print(max(resultados))
    print(sum(resultados)/len(resultados))

if __name__ == "__main__":
    main()
    
    

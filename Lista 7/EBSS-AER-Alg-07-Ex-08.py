'''Bingo: verificando uma cartela vencedora. Uma cartela de bingo vencedora deve conter
uma linha (ou coluna ou diagonal) com 5 números que foram sorteados. Normalmente, nas
cartelas de papel, os jogadores fazem um X sobre o número sorteado. Na sua implementação
(no seu dicionário representando a cartela), vamos substituir por 0 o número que foi sorteado.
Escreva uma função que receba como único parâmetro um dicionário representando uma
cartela. Se a cartela contiver uma linha, coluna ou diagonal preenchida com zeros, a função
deve retornar True. Caso contrário deve retornar False. Crie um programa que demonstre o
funcionamento da sua solução criando e exibindo várias cartelas de bingo e indicando se cada
uma é ou não é vencedora. Você deve mostrar pelo menos uma cartela com linha horizontal,
uma com linha v ertical, uma com diagonal e por fim uma com alguns zeros cruzados, mas
que não é vencedora. Você pode usar sua solução do problema anterior como ponto de
partida para este exercício. Dica: como a cartela não tem números negativos, encontrar uma
sequencia de 5 zeros é análogo a descobrir se a soma de uma sequencia de 5 números é
igual a zero. Talvez você ache mais fácil fazer desse jeito.'''


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
    print(cartela)
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
        
        
def main():
    cartela = gerar_cartela()
    cartela_vert= {"B":[19, 20, 23, 25, 30],'I': [0,0,0,0,0], 'N': [33, 35, 36, 38, 43], 'G': [47, 50, 56, 57, 60], 'O': [61, 62, 68, 70, 71]}
    cartela_hor = {'B': [0, 8, 9, 12, 13], 'I': [0, 20, 23, 25, 30], 'N': [0, 35, 36, 38, 43], 'G': [0, 50, 56, 57, 60], 'O': [0, 62, 68, 70, 71]}
    cartela_diag = {'B': [0, 8, 9, 12, 13], 'I': [19, 0, 23, 25, 30], 'N': [33, 35, 0, 38, 43], 'G': [47, 50, 56, 0, 60], 'O': [61, 62, 68, 70, 0]}
    cartela_perdida = {'B': [0, 0, 0, 0, 13], 'I': [0, 20, 23, 25, 30], 'N': [0, 35, 36, 38, 43], 'G': [0, 50, 56, 57, 60], 'O': [61, 62, 68, 70, 71]}
    exibir_cartela(cartela_perdida)
    print(verificar_vencedor(cartela_perdida))

if __name__ == "__main__":
    main()
    
    

'''Busca reversa. Escreva uma função chamada buscaReversa, que encontra todas as chaves
de um dicionário que estão mapeadas para um determinado valor. A função deve receber
como parâmetros um dicionário e um valor para ser buscado no dicionário. A função deve
retornar uma lista (possivelmente vazia) com as chaves encontradas. Escreva uma função
main para demonstrar sua função. Note que a função deve funcionar independentemente de
ela retornar múltiplas chaves, uma única chave, ou nenhuma chave.'''

def buscaReversa(dict,valores):
    keys = []
    for chave,valor in dict.items():
        if valor == valores:
            keys.append(chave)
    return keys

def main():
    x = { 
        "Messi" : "Ponta",
        "Cristiano" : "Ataque",
        "Iniesta": "Meio",
        "Xavi" : "Meio",
        "Neymar" : "Ponta",
        "Mbappe" : "Ataque" ,
        "Ronaldinho" : "DEUS"
        }
    
    valor = "Ponta"
    print(buscaReversa(x,valor))
    


if __name__ == "__main__":
    main()
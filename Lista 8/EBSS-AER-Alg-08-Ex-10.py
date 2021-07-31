'''Decodificação run-lenght. A codificação run-length é uma técnica simples de compressão de
dados que pode ser eficaz quando valores repetidos ocorrem em posições adjacentes dentro
de uma lista. Compressão é obtida substituindo grupos de valores repetidos por uma cópia do
valor, seguido pelo número de vezes que o valor deve ser repetido. Por exemplo, a lista ["A",
"A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B",
"A", "A", "A", "A", "A", "A", "B"] seria comprimida como ["A", 12, "B", 4, "A",
6, "B", 1]. A descompressão é realizada replicando cada valor da lista o número de vezes
indicado.
Escreva uma função recursiva que descompacte uma lista codificada run-lenght. Sua função
recursiva deve ter uma lista compactada em run-lenght como seu único parâmetro. Ela deve
retornar a lista descompactada como seu único resultado. Crie um programa principal que
exibe uma lista codificada em run-lenght e o resultado da decodificação.'''


def mapear(x):
    if type(x) == int:
        return x

def run_lenght(lista):
    resultado = map(mapear,lista)
    lista_result = list(resultado)
    lista_result = set(lista_result)
    lista_result.remove(None)
    lista_result = list(lista_result)
    if lista_result.count(1)==1:
        lista_result.remove(1)
        lista.remove(1)
        if lista_result != []:
            a = lista.pop(0)
            b = lista.pop(0)
            lista.append(a)
            lista.append(b)
            return run_lenght(lista)
        else:
            lista.reverse()
            return lista
    else:
        if lista_result[-1]>0:
            lista.insert(-2,lista[-2])
            lista[-1] = lista[-1]-1

            return run_lenght(lista)



def main():
    print(f'Original = ["A",10,"B",5,"C",1]')
    print(f'Decodificada = {run_lenght(["A",10,"B",5,"C",1])}')

if __name__ == "__main__":
    main()
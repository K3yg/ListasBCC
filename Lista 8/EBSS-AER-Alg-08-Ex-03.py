'''Palíndromo. Faça uma função Python recursiva que recebe uma string e retorne um valor
lógico indicando se ela é ou não é um palíndromo. OBS: Um palíndromo é uma palavra ou
frase, que é igual quando lida da esquerda para a direita ou da direita para a esquerda
(Espaços em branco e sinais de pontuação devem ser descartados). Exemplo de palíndromo:
"saudavel leva duas”.'''

def palindromo(frase):

    def letras(frase):
        frase = frase.lower()
        resposta = ''
        for letra in frase:
            if letra in 'abcdefghijklmnopqrstuvwxyz':
                resposta = resposta + letra
        return resposta

    def e_palindromo(frase):
        if len(frase) <= 1:
            return True
        else:
            return frase[0] == frase[-1] and e_palindromo(frase[1:-1])

    return e_palindromo(letras(frase))


print(palindromo('saudavel leva duas'))


 

def verificaPrecedencia(operador):
    p1 = "+-"
    p2 = "/*"
    p3 = "^"
    if operador in p1:
        precedencia = 1
    elif operador in p2:
        precedencia = 2
    elif operador in p3:
        precedencia = 3
    else:
        precedencia = -1

    return precedencia

def tokeniza_postfix(infix):
    operadores = []
    postfix = []
    for token in infix:
        if type(token) == int:
            postfix.append(token)
        if token in ["*","/","^","+","-"]:
            if len(operadores) > 0:
                while len(operadores) >= 0 and operadores[-1] != "(" and verificaPrecedencia(token) < verificaPrecedencia(operadores[-1]):

                    postfix.append(operadores[-1])
                    operadores.pop(-1)
            operadores.append(token)
        if token == "(":
            operadores.append(token)
        if token == ")":
            while operadores[-1] != "(":
                postfix.append(operadores[-1])
                operadores.pop(-1)
            operadores.pop(-1)
    while len(operadores) > 0:
        postfix.append(operadores[-1])
        operadores.pop(-1)

    return postfix
        

def tokeniza(expressao):
    expressao = expressao.replace(" ", "")
    listaTokens = []
    tokens = "*/^()"
    tokens2 = "+-"
    token = ""
    for i in range(len(expressao)):
        if expressao[i] in tokens2:
            if expressao[i-1].isnumeric() or expressao[i-1] in tokens:
                if token != "":
                    listaTokens.append(int(token))
                    token = ""
                listaTokens.append(expressao[i])
            else:
                token += expressao[i]

        elif expressao[i] in tokens:
            if token != "":
                    listaTokens.append(token)
                    token = ""
            listaTokens.append(expressao[i])
            
        
        elif expressao[i].isnumeric():
            token += expressao[i]
    if token != "":
        listaTokens.append(int(token))

    return(listaTokens)


def main():
    x = input("Digite a expressão: ")
    print(tokeniza_postfix(tokeniza(x)))

if __name__ == "__main__":
    main()


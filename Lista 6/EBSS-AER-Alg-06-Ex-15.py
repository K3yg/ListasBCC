def tokeniza(expressao):
    expressao = expressao.replace(" ", "")
    listaTokens = []
    tokens = "*/^()"
    tokens2 = "+-"
    token = ""
    for i in range(len(expressao)):
        if expressao[i] in tokens2:
            print(expressao[i])
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
    print(tokeniza(x))

if __name__ == "__main__":
    main()
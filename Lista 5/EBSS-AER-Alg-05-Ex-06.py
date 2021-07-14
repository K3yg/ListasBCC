def centralizar_string(string,largura):
    arruma = (largura-len(string))//2
    a = ""
    for i in range(arruma):
        a = a + " "
    a = a + string
    return a    


def main():
    largura = int(input("DIgite a largura do terminal"))
    string = str(input("Digite qualquer coisa"))
    print(centralizar_string(string,largura))


if __name__ == "__main__":
    main()
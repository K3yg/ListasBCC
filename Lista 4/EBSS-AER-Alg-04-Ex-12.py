print("\t 1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9\t 10")
for i in range(10):
    linha = f"{i+1}"
    atual = 0
    for x in range(10):
        atual += i+1
        linha += f"\t {atual}"
    print(linha)
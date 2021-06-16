palavra = input("Insira uma palavra: ")
nova = ""
for i in palavra:
    nova = i +  nova
if palavra == nova:
    print(f"É um palíndromo: {palavra} --> {nova}")
else:
    print(f"Não é um palíndromo: {palavra} --> {nova}")
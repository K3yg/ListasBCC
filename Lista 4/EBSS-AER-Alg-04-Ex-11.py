frase = input("Insira uma frase: ")
nova = ""
nova2 = ""
novafrase = ""
for i in frase:
    if (ord(i) >= 65 and ord(i) <= 90) or ord(i) >= 97 and ord(i) <= 122:
        novafrase += i
        nova2 = i +  nova2
    nova = i + nova
if novafrase.lower() == nova2.lower():
    print(f"É um palíndromo: {frase} --> {nova}")
else:
    print(f"Não é um palíndromo: {frase} --> {nova}")
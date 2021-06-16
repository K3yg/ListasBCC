from random import randint
somageral = 0
for i in range(10):
    resultados = ""
    contacara = 0
    contacoroa = 0
    contatudo = 0
    while contacara < 3 and contacoroa < 3:
        x = randint(1,2)
        if x == 1:
            resultados += "A "
            contacara += 1
            contacoroa = 0
        else:
            resultados += "O "
            contacoroa += 1
            contacara = 0
        contatudo += 1
    print(f"{resultados} ({contatudo} Sorteios)")
    somageral += contatudo
print(f"Na média, foram necessários {somageral/10} sorteios.")
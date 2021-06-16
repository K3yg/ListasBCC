x = input("Insira um número em binário: ")
contador = 0
dec = 0
for i in x:
    contador += 1
    dec += int(i) * 2 ** (len(x) - contador)
    
print(dec)
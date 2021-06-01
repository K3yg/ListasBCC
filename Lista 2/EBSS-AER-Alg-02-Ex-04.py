
#Obter os 3 valores
x = int(input('Insira um número inteiro: '))
y = int(input('Insira outro número inteiro: '))
z = int(input('Insira mais um número inteiro: '))

#usar min e max
maior = max(x,y,z)
menor = min(x,y,z)

#calcular a media pra descobrir o meio
media =  (x+y+z)/3

#printar
print(f'{menor}, {int(media)}, {maior}')
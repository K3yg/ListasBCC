suco = float(input('Qual o valor do suco? '))
principal = float(input('Qual o valor do prato princialp? '))
sobremesa = float(input('Qual o valor da sobremesa? '))

preço = suco + principal + sobremesa

taxa = preço*0.10

result = preço + taxa

print(f'O valor final é de R${result:.2f}')
'''
Calculando o troco. Considere o software que controla uma máquina automática de compras.
Uma tarefa que ele precisa realizar é determinar quanto troco fornecer ao comprador quando
este faz o pagamento em dinheiro. Escreva um programa Python que inicia lendo do usuario
uma quantidade de centavos como um número inteiro (portanto vamos considerar números de
0 a 99). Então o seu programa deve calcular e exibir quantidade e o valor de cada moeda para
compor este troco em centavos informado. O troco deve ser montado com a menor quantidade
possível de moedas. Assuma que a máquina possui moedas de 50, 25, 10, 5 e 1 centavos.
'''
centavos = int(input("Diga os centavos: "))
 
moeda50 = centavos//50
moeda25 = (centavos - (moeda50*50))//25
moeda10 = (centavos - (moeda50*50) - (moeda25*25))//10
moeda5 = (centavos - (moeda50*50) - (moeda25*25) - (moeda10*10))//5
moeda1 = (centavos - (moeda50*50) - (moeda25*25) - (moeda10*10) - (moeda5*5) )//1
 
print(f'moedas 50 - {moeda50}')
print(f'moedas 25 - {moeda25}')
print(f'moedas 10 - {moeda10}')
print(f'moedas 5 - {moeda5}')
print(f'moedas 1 - {moeda1}')

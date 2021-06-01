data = int(input('Digite a data a seguir (DDMMAA): '))
 
anos = data%100
meses = (data%10000 - anos)//100
dias = (data - meses - anos)//10000
 
datainvertida = anos * 10000 + meses *100+ dias
 
print('Data: {}, data invertida: {}'.format(data, datainvertida))
import math

#ler 2 inteiros
a = int(input('Insira o primeiro valor inteiro (a): '))
b = int(input('Insira o segundo valor inteiro (b): '))

#soma de a e b
soma = a + b
print(f'A soma dos inteiros é: {soma}')

#diferença entre b e a
sub = b - a 
print(f'A diferença de b e a é de: {sub}')

#produto a por b
prod = a * b
print(f'O produto de a por b é: {prod}')

#o quociente de quando a é dividido por b
div = a / b
print(f'O quociente de a por b é: {div}')

#log10a
log = math.log10(a) 
print(f'O log de a é: {log}')

#a**b
pot = a**b
print(f'O valor de a elevado a b é de: {pot}')
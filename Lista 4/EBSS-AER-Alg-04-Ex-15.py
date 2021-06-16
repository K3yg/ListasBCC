x = int(input("Insira um número para realizar a conversão: "))
result = ""
while x != 0:
    r = x % 2
    result = str(r) + result
    x //= 2
print(result)
from random import randint

def criar_senha():
    senha = ""
    comprimento = randint(7,10)
    for i in range(comprimento):
        senha = senha + chr(randint(33,126))
        
    return senha

def main():
    print(criar_senha())
    
if __name__ == "__main__":
    main()
def isInteger(string):
    string = string.strip()
    try: 
        int(string)
        return True
    except ValueError:
        return False

def main():
    string = input("Digite")
    print(isInteger(string))


if __name__ == "__main__":
    main()
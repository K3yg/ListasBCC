print(" _______________________________")
print("|    Celcius\t|    Farenheit\t|")
print(" -------------------------------")
for c in range(100):
    if (c + 1) % 10 == 0:
        f = (c + 1) * 1.8 + 32
        print(f"|\t{c+1}\t|\t{f:.0f}\t|")
print(" -------------------------------")
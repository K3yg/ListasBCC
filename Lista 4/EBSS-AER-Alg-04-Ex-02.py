precos = ["R$ 4.95", "R$ 9.95", "R$ 14.95", "R$ 19.95", "R$ 24.95"]
for i in precos:
    temp = float(i[2:]) * 0.6
    print(f"| {i} \t| R$ {temp:.2f} \t|")
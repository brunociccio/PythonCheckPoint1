erro = False
a = float(input("A = "))
if a != 0:
    b = float(input("B = "))
    c = float(input("C = "))
    delta = b ** 2 - 4 * a * c
    print(f"Delta = {delta}")
    if delta < 0:
        print("Não há raiz quadrada negativa!")
        erro = True
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Raizes iguais: x1 = x2 = {x:.2f}")
    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        print(f"Raizes distintas: x1 = {x1:.2f} e x2 = {x2:.2f}")
    if not erro:
        if b == 0 or c == 0:
            print("Equação incompleta do segundo grau!")
        else:
            print("Equação completa de segundo grau!")
else:
    print("Não é uma equação de segundo grau!")
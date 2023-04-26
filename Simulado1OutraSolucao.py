# Definindo as variáveis para armazenar as notas dos checkpoints, sprints e global solutions
notas_cp1 = 0
notas_cp2 = 0
notas_cp3 = 0
notas_sp1 = 0
notas_sp2 = 0
notas_gs = 0

# Obtendo as notas do usuário para cada checkpoint
while True:
    notas_cp1 = float(input("Insira a nota do primeiro checkpoint (0-10): "))
    if notas_cp1 >= 0 and notas_cp1 <= 10:
        break
while True:
    notas_cp2 = float(input("Insira a nota do segundo checkpoint (0-10): "))
    if notas_cp2 >= 0 and notas_cp2 <= 10:
        break
while True:
    notas_cp3 = float(input("Insira a nota do terceiro checkpoint (0-10): "))
    if notas_cp3 >= 0 and notas_cp3 <= 10:
        break

# Obtendo as notas do usuário para cada sprint
while True:
    notas_sp1 = float(input("Insira a nota do primeiro sprint (0-10): "))
    if notas_sp1 >= 0 and notas_sp1 <= 10:
        break
while True:
    notas_sp2 = float(input("Insira a nota do segundo sprint (0-10): "))
    if notas_sp2 >= 0 and notas_sp2 <= 10:
        break

# Obtendo a nota do usuário para o global solution
while True:
    notas_gs = float(input("Insira a nota do global solution (0-10): "))
    if notas_gs >= 0 and notas_gs <= 10:
        break

# Calculando a média das notas dos checkpoints
notas_cp = [notas_cp1, notas_cp2, notas_cp3]
notas_cp.remove(min(notas_cp)) # Removendo a menor nota dos checkpoints
media_cp = sum(notas_cp) / len(notas_cp)

# Calculando a média das notas dos sprints
media_sp = (notas_sp1 + notas_sp2) / 2

# Calculando a média final, considerando os pesos de cada semestre
media_final = (media_cp * 0.2) + (media_sp * 0.2) + (notas_gs * 0.6)

# Exibindo a média final
print("A sua média final é:", media_final)
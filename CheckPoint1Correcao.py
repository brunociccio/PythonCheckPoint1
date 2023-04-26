print(f"Abaixo digite as notas de seus check points, sprints e global solution referente ao "
      f"primeiro semestre")
cp1sem1 = float(input(f"Digite a nota do seu primeiro Check Point: "))
if cp1sem1 >= 0 and cp1sem1 <= 10:
    cp2sem1 = float(input(f"Digite a nota do seu segundo Check Point: "))
    if cp2sem1 >= 0 and cp2sem1 <= 10:
        cp3sem1 = float(input(f"Digite a nota do seu terceiro Check Point: "))
        if cp3sem1 >= 0 and cp3sem1 <= 10:
            medcp1sem = (cp1sem1 + cp2sem1)/2
            if cp1sem1 < cp2sem1:
                medcp1sem = (cp2sem1 + cp3sem1)/2
            if cp1sem1 > cp2sem1:
                medcp1sem = (cp1sem1 + cp3sem1) / 2
            if cp1sem1 > cp3sem1 and cp2sem1 > cp3sem1:
                medcp1sem = (cp1sem1 + cp2sem1) / 2
            print(f"A média dos Check Points é de '{medcp1sem}'")
        else:
            print(f"A nota do tereiro Check Point '{cp3sem1}' é inválida!")
    else:
        print(f"A nota do segundo Check Point '{cp2sem1}' é inválida!")
else:
    print(f"A nota do primeiro Check Point '{cp1sem1}' é inválida!")

sp1sem1 = float(input(f"Digite a nota do seu primeiro Sprint: "))
if sp1sem1 >= 0 and sp1sem1 <= 10:
    sp2sem1 = float(input(f"Digite a nota do seu segundo Sprint: "))
    if sp2sem1 >= 0 and sp2sem1 <=10:
        medsp1sem = (sp1sem1 + sp2sem1) / 2
        print(f"A média dos seus Sprints é de '{medsp1sem}'")
    else:
        print(f"A nota do seu segundo Sprint '{sp2sem1}' é inválida!")
else:
    print(f"A nota do seu primeiro Sprint '{sp1sem1}' é inválida!")

gs1sem = float(input(f"Digite a nota do seu Global Solution: "))
if gs1sem >= 0 and gs1sem <= 10:
    gs1sem = gs1sem
else:
    print(f"A nota do seu Global Solution '{gs1sem}' é inválida!")

medSem1 = (medcp1sem * 0.2) + (medsp1sem * 0.2) + (gs1sem * 0.6)
print(f"A sua nota referente ao primeiro semestre é de '{medSem1:.2f}'")

print(f"Abaixo digite as notas de seus check points, sprints e global solution referente ao "
      f"segundo semestre")

cp1sem2 = float(input(f"Digite a nota do seu primeiro Check Point: "))
if cp1sem2 >= 0 and cp1sem2 <= 10:
    cp2sem2 = float(input(f"Digite a nota do seu segundo Check Point: "))
    if cp2sem2 >= 0 and cp2sem2 <= 10:
        cp3sem2 = float(input(f"Digite a nota do seu terceiro Check Point: "))
        if cp3sem2 >= 0 and cp3sem2 <= 10:
            medcp2sem = (cp1sem2 + cp2sem2)/2
            if cp1sem2 < cp2sem2:
                medcp2sem = (cp2sem2 + cp3sem2)/2
            if cp1sem2 > cp2sem2:
                medcp2sem = (cp1sem2 + cp3sem2) / 2
            if cp1sem2 > cp3sem2 and cp2sem2 > cp3sem2:
                medcp1sem = (cp1sem2 + cp2sem2) / 2
            print(f"A média dos Check Points é de '{medcp2sem}'")
        else:
            print(f"A nota do tereiro Check Point '{cp3sem2}' é inválida!")
    else:
        print(f"A nota do segundo Check Point '{cp2sem2}' é inválida!")
else:
    print(f"A nota do primeiro Check Point '{cp1sem2}' é inválida!")

sp1sem2 = float(input(f"Digite a nota do seu primeiro Sprint: "))
if sp1sem2 >= 0 and sp1sem2 <= 10:
    sp2sem2 = float(input(f"Digite a nota do seu segundo Sprint: "))
    if sp2sem2 >= 0 and sp2sem2 <=10:
        medsp2sem = (sp1sem2 + sp2sem2) / 2
        print(f"A média dos seus Sprints é de '{medsp2sem}'")
    else:
        print(f"A nota do seu segundo Sprint '{sp2sem2}' é inválida!")
else:
    print(f"A nota do seu primeiro Sprint '{sp1sem2}' é inválida!")

gs2sem = float(input(f"Digite a nota do seu Global Solution: "))
if gs2sem >= 0 and gs2sem <= 10:
    gs2sem = gs2sem
else:
    print(f"A nota do seu Global Solution '{gs2sem}' é inválida!")

medSem2 = (medcp2sem * 0.2) + (medsp2sem * 0.2) + (gs2sem * 0.6)
print(f"A sua nota referente ao segundo semestre é de '{medSem2:.2f}'")

medAnual = (medSem1 * 0.4) + (medSem2 * 0.6)
print(f"A sua média anual é de '{medAnual:.2f}'")

print(f"""
    - - - Resumo das Notas - - -
    Primeiro Semestre....: {medSem1: 4.2f} 
    Segundo Semestre.....: {medSem2: 4.2f}
    Nota Anual...........: {medAnual: 4.2f}
    A nota anual tem como valor o peso de 40% do 
    primeiro semestre e 60% do segundo semestre 
""")

print(f"Obrigado por usar nosso sistema!")
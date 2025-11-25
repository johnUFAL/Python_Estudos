N1 = float(input("Digite a nota N1: "))
N2 = float(input("Digite a nota N2: "))
N3 = float(input("Digite a nota N3: "))

media = (N1+N2+N3)/3

if media >= 7:
     situacao = "Aprovado"
elif 5 <= media < 7:
     situacao = "Recuperação"
else:
     situacao = "Reprovado"

print(f"Média: {media:.1f}")
print(f"Situação {situacao}")
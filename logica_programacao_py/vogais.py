
arr = str(input("Digite uma frase: ")).lower().strip()
if not arr:
    print("ERRO: Digite uma frase válida!")
    exit()

a = e = i = o = u = 0

for ch in arr:
    if ch == "a":
        a += 1
    elif ch == "e":
        e += 1
    elif ch == "i":
        i += 1
    elif ch == "o":
        o += 1
    elif ch == "u":
        u += 1

print(f'a: {a}')
print(f'e: {e}')
print(f'i: {i}')
print(f'o: {o}')
print(f'u: {u}')

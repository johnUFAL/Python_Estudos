import math

try:
    num = int(input("Digite um número: "))
except ValueError:
    print("Erro: Digite um número inteiro válido!")
    exit()

if num <= 1:
    primo =False
elif num == 2:
    primo = True
elif num % 2 == 0:
    primo = False
else:
    primo = True
    raiz = math.isqrt(num) #isqrt retorna a raiz inteira
    for div in range(3, raiz+1, 2): #começa no 3 pulando += 2 e vai até raiz+1 
        if num%div == 0:
            primo = False
            break
        
print(f"{num} {'é primo' if primo else 'não é primo'}")

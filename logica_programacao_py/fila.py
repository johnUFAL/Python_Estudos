def enfileirar(fila, x):
    fila.append(x)
    print(f'Fila atual: {fila}')

def desenfileirar(fila):
    if fila:
        x = fila.pop()
        print(f"Item removido: {x}")
        print(f'Fila atual: {fila}')
        return x
    else:
        print("Fila vazia!")
        return None

def tamanho(fila):
    tam = len(fila)
    print(f'Tamanho atual: {tam}')
    return tam

fila = []
while True:
    opcao = str(input("Digite: 'add' para enfileirar 'remover' para desenfileirar 'tam' para informar o tamanho e 'sair' para fechar: ")).strip().lower()

    if opcao == 'sair':
        print("Fim!")
        break
    elif opcao == 'add':
        try:
            x = int(input())
            enfileirar(fila, x)
        except ValueError:
            print("ERRO: Digite um numero válido!")
    elif opcao == 'remover':
        desenfileirar(fila)
    elif opcao == 'tam':
        tamanho(fila)
    else: 
        print("Opcão invalida")

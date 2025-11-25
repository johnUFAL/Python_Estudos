def remover_lista(lista, item):
    if item in lista:
        lista.remove(item)
        print(f"Item '{item}' removido!")
    else:
        print(f"Item '{item}' não encontrado.")

def adicionar_lista(lista, item):
    lista.append(item)
    print(f"Lista: {lista}")

lista_de_compra = []
while True:
    new = str(input("Digite 'add' para adicionar, 'remover' para excluir ou 'sair': ")).lower().strip()
    
    if new == 'sair':
        print("Finalizado!")
        break
    elif new == 'add':
        item = input().strip().lower()
        adicionar_lista(lista_de_compra, item)
    elif new == 'remover':
        item = input().strip().lower()
        remover_lista(lista_de_compra, item)
    else:
        print("Opcão invalida")

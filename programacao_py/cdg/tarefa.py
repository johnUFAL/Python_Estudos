tarefas = []

def adicionar():
    tarefa = {
        "Nome": input("Digite o nome da tarefa: ").capitalize().strip(),
        "Sub": {
            "Descrição": input("Digite a descrição da tarefa: ").capitalize().strip(),
            "Status": input("Digite o status da tarefa: ").capitalize().strip()
        }
    }
    
    tarefas.append(tarefa)
    print(f"Tarefa {tarefa['Nome']} adicionada!\n")

def listar():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa['Nome']}")
        for k, v in tarefa["Sub"].items():
            print(f"    {k}: {v}")
        print("-"*20)
    print("\n")

def conclusao(nome):
    for tarefa in tarefas:
        if tarefa['Nome'] == nome:
            tarefa["Sub"]['Status'] = "concluído"
            print(f"Tarefa {tarefa['Nome']} concluída")
            return 
    print(f"{nome} não encontrada!")

def remover(nome):
    for tarefa in tarefas:
        if tarefa['Nome'] == nome:
            tarefas.remove(tarefa)
            print(f"Tarefa {nome} removida")
            return
    print(f"Tarefa {nome} não encontrada")

def main():
    while True: 
        print("Digite uma das opções: ")
        print("1 - Adiciona tarefa.\n2 - Listar todas as tarefas.\n3 - Marcar como concluída.\n4 - Remover tarefa.\n5 - Sair")

        try: 
            opc = int(input("Opção: "))
        except ValueError:
            print("Opção inválida.")
            continue
        
        if opc == 1:
            adicionar()
        elif opc == 2:
            listar()
        elif opc == 3:
            nome = input("Digite o nome da tarefa: ").capitalize().strip()
            conclusao(nome)
        elif opc == 4:
            nome = input("Digite o nome da tarefa: ").capitalize().strip()
            remover(nome)
        elif opc == 5:
            print("Encerrando...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == '__main__':
    main()

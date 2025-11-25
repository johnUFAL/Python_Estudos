import json
import os

def main():
    pessoa = {
        "nome": input("Digite seu nome: ").capitalize().strip(),
        "idade": int(input("Digite sua idade: ")),
        "cidade": input("Digite sua cidade: ").capitalize().strip()
    }
    
    if os.path.exists("test.json"):
        with open("test.json", 'r', encoding='utf-8') as arquivo:
            try:
                dados = json.load(arquivo)
            except json.JSONDecodeError:
                dados = []
    else:
        dados = []

    dados.append(pessoa)

    with open('test.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=1, ensure_ascii=False)

    print("Dados adicionados com sucesso")

if __name__ == '__main__':
    main()

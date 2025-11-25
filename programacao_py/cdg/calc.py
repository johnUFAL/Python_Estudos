def calcula(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b ==0:
            raise ValueError("Intederminação!")
        return a / b
    else:
        raise ValueError("ERRO: Operação inválida!")
        
        
def main():
    print("Digite dois números: ")
    try: 
        a = float(input())
        b = float(input())
    except ValueError:
        print("ERRO: Espera-se apenas números!")
        exit()

    print("Escolha sua operação:")
    print("'+' - Adição.\n'-' - Subtração.\n'*' - Multiplicação.\n'/' - Divisão")

    opc = input().strip()
    try:
        resp = calcula(a, b, opc)
        print(f"{a} {opc} {b} = {resp}")
    except ValueError as e:
        print(f"Erro {e}")

if __name__ == '__main__':
    main()

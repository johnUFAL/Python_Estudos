def main():
    while True:
            try:
                num = int(input("Digite um número inteiro: "))
                break
            except ValueError:
                print("Apenas números inteiros.")
                continue
    for i in range(0, 11):
        valor = i * num
        print(f"{num} x {i} = {valor}\n") 

if __name__ == '__main__':
     main()
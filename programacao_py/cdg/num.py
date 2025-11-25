def main():
    while True:
        try:
            num = float(input("Digite um número: "))
            break
        except ValueError:
            print("Apenas valor numérico")
            continue

if __name__ == '__main__':
    main()
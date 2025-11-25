def palindromo(string):
    return string == string[::-1]
  
def main():
    print("Digite uma palavra ou frase: ")
    string =  input().lower().replace(" ", "")
  
    if palindromo(string):
        print(f"A string: {string} é um palíndromo")
    else: 
        print(f"A string: {string} não é um palíndromo")
   
if __name__ == '__main__':
    main()

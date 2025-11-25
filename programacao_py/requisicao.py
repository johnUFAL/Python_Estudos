import requests

def main():
    url = 'https://www.python.org'
    resposta = requests.get(url)
    print(resposta)

    if resposta.status_code == 200:
        print(resposta.text)

if __name__ == '__main__':
    main()
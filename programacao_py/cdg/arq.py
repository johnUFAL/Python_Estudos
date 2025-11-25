import json
import string

def contador_palavras(arquivo):
    try:
        # Abrindo arquivo json para leitura com métodos: 'r', load()
        with open(arquivo, 'r', encoding='utf-8') as f:
            txt = f.read()
        
        txt = txt.translate(str.maketrans('', '', string.punctuation)).lower()

        palavras = txt.split()
        freq = {}
        for palavra in palavras:
            freq[palavra] = freq.get(palavra, 0 + 1)
        return freq
    except FileExistsError:
        print(f"ERRO: O arquivo {arquivo} não foi achado")
        return {}
    except Exception as e:
        print(f'ERRO: processamento de arquivo: {e}')
        return {}

def main():
    nome_arq = input("Digiteo nome do arqquivo de texto: ")
    freq_palavras = contador_palavras(nome_arq)

    if freq_palavras:
        print("\nFrequência: ")
        for palavra, freq in sorted(freq_palavras.items()):
            print(f"{palavra}: {freq}")
    else:
        print("Não foi possível contar as palavras")

if __name__ == '__main__':
    main()

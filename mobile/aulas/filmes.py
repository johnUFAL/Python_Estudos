import requests

API_KEY = "6bdf6ea3124293940bfbbf5bfdb6164e"

BASE_URL = "https://api.themoviedb.org/3"

def busca_filme_por_titulo(titulo):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={titulo}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        if dados['results']:
            primeiro_filme = dados['results'][0]
            nome = primeiro_filme['title']
            sinopse = primeiro_filme.get('overview', 'Sinopse não disponível.')
            data_lancamento = primeiro_filme.get('release_date', 'Data não disponível.')

            print(f"Nome: {nome}")
            print(f"Sinopse: {sinopse}")
            print(f"Data de lançamento: {data_lancamento}")
        else:
            print("Filme não encontrado!")
    else:
        print(f"ERRO: Ao acessar a API: {resposta.status_code}")

busca_filme_por_titulo("Pacific Rim")

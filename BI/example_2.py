import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# Gerando set de dados
np.random.seed(42)
num_vendas = 30
data_inicio = datetime(2023, 7, 1)
produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D']

dados_vendas = {
    "Data da Venda": [data_inicio + timedelta(days=np.random.randint(0, 30)) for _ in range(num_vendas)],
    "Produto":np.random.choice(produtos, num_vendas),
    "Quantidade Vendida": np.random.randint(1, 10, num_vendas),
    "Valor Total da Venda": np.random.randint(100, 1000, num_vendas)
}

df = pd.DataFrame(dados_vendas)

# Imprimindo as cinco primeiras linhas
print(dados_vendas.head())

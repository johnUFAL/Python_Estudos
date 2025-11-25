import pandas as pd

dados_vendas = {
    "Data da Venda": ["2023-07-01", "2023-07-05", "2023-08-12", "2023-08-15"],
    "Produto": ["Produto A", "Produto B", "Produto A", "Produto C"],
    "Quantidade Vendida": [10, 5, 8, 3],
    "Valor Total da Venda": [100, 50, 80, 30]
}

# Converter para formato data
df = pd.DataFrame(dados_vendas)
df["Data da Venda"] = pd.to_datetime(df["Data da Venda"])
df["Mês da Venda"] = df["Data da Venda"].dt.strftime('%Y-%m')

# Agrupando por produto e mês somando as quantidades vendidas e o valor total
tabela_agregada = df.groupby(["Produto", "Mês da Venda"]).agg({
    "Quantidade Vendida": "sum",
    "Valor Total da Venda": "sum"
}).reset_index()

print(tabela_agregada)

print(df.info())
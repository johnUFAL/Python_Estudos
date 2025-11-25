import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = "C:\Users\Joao Duarte\Desktop\data\campoes_brasileiro.csv"
df = pd.read_csv(data)

# Primeiras linhas
print(df.head())

# Informações
print(df.info())

# Est. Descritiva
print(df.describe())

# NULL
print(df.isnull().sum())

# Preencher com 0
# df = df.dillna(0)


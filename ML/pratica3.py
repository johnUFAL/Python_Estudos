import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import numpy as np

# Geração de dados
X_reg = pd.DataFrame({'tamanho': [50, 60, 70, 80, 90], 'idade': [10, 12, 15, 20, 25]})
y_reg = [300, 400, 500, 600, 700]

# Classificação Iris
iris = load_iris()
X_class, y_class = iris.data, iris.target

# Treino do modelo de regressão linear
regressor = LinearRegression()
regressor.fit(X_reg, y_reg)
pred = regressor.predict([[85, 18]]) # prrevisão para uma casa de 85m² e 18 anos
print(f'Previsão ')

# Treino do modelo de Arvore de decisão
X_train, X_test, y_train, y_test = train_test_split(X_class, y_class, test_size=0.2, random_state=42)
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
accuracy = classifier.score(X_test, y_test)
print(f'Acurácia no conjunto de teste: {accuracy:.2f}')

# Visuzalização
# plot dos pontos de dados e a linha de regressão
plt.scatter(X_reg['tamanho'], y_reg, color='blue', label='Dados Reais')
plt.plot(X_reg['tamanho'], regressor.predict(X_reg), color='red', label='Linha de Regressão')

# Destaque dos pontos de previsão
plt.scatter(85,regressor.predict([[85, 18]]), color='green', s=100, label='Ponto de Previsão')

# Configurando gráfico
plt.title('Regressão Linear - Previsão de Preço de Imóveis')
plt.xlabel('Tamanho (m2)')
plt.ylabel('Preço (mil)')
plt.legend()
plt.grid(True)
plt.show()

#Fazer previsões no conjunto de teste
y_pred = classifier.predict(X_test)

#Visualizar a matriz de confusão
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='g')
plt.title('Matriz de Confusão - Classificação com Árvore de Decisão')
plt.xlabel('Previsão')
plt.ylabel('Valor Real')
plt.show()

#Visualizar as previsões de uma característica (exemplo: largura da pétala versus comprimento da pétala)
plt.scatter(X_test[:, 2], X_test[:, 3], c=y_pred, cmap='viridis', label='Previsão')
plt.scatter(X_test[:, 2], X_test[:, 3], c=y_test, edgecolor='red', label='Valor Real', marker='x')

#Configurar o gráfico
plt.xlabel('Largura da Pétala')
plt.ylabel('Comprimento da Pétala')
plt.title('Visualização das Previsões - Dataset Iris')
plt.legend()
plt.grid(True)
plt.show()
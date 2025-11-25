#importar as bibliotecas necessárias
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error

#carregar o dataset California Housing
california = fetch_california_housing()
X, y = california.data, california.target

#dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)

#definir o modelo e os parâmetros para grid search
parameters = {'alpha': [0.01, 0.1, 1.0, 10]}
lasso = Lasso()

#Aplicar Grid Search com validação cruzada de 4 folds
grid_search = GridSearchCV(lasso, parameters, cv=5)
grid_search.fit(X_train, y_train)

#Melhor parâmetro encontrado
print(f"Melhor parâmetro encontrado: {grid_search.best_params_}")

#treinar o modelo com o melhor parâmetro
best_lasso = grid_search.best_estimator_
best_lasso.fit(X_train, y_train)

#fazer previsões no conjunto de teste
y_pred = best_lasso.predict(X_test)

#calcular e exibir o erro médio absoluto (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f"Erro Médio Absoluto (MAE) no Conjunto de Teste: {mae:.2f}")
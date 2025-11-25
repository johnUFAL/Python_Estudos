from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Imporntando o dataset digits
digits = datasets.load_digits()

# Vizualizando
plt.imshow(digits.images[0], cmap='grey')
plt.title(f'Label: {digits.target[0]}')
plt.show()

# Treinando model de classificação
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

model = SVC(gamma=0.001)
model.fit(X_train, y_train)

# avaliando o desempenho
accuracy = model.score(X_test, y_test)
print(f'Acurácia do Modelo: {accuracy:.2f}')
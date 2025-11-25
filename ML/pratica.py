from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

cancer = datasets.load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.2, random_state=42)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f'Acurácia do Modelo: {accuracy:.2f}')
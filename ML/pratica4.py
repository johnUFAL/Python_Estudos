from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

# Carregando dataset
iris = load_iris()
X, y = iris.data, iris.target

# Divisão dos dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Modelo Decision Tree
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)
y_pred_dt = dt_model.predict(X_test)

#Modelo SVM
svm_model = SVC()
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)

#Méricas para o Decision Tree
print("Decision Tree:")
print(f"Acurácia: {accuracy_score(y_test, y_pred_dt):.2f}")
print(f"Precisão: {precision_score(y_test, y_pred_dt, average='macro'):.2f}")
print(f"Recall: {recall_score(y_test, y_pred_dt, average='macro'):.2f}")
print(f"F1-Score: {f1_score(y_test, y_pred_dt, average='macro'):.2f}")

#Métricas para o SVM
print("SVM: ")
print(f"Acurácia: {accuracy_score(y_test, y_pred_svm):.2f}")
print(f"Precisão: {precision_score(y_test, y_pred_svm, average='macro'):.2f}")
print(f"Recall: {recall_score(y_test, y_pred_svm, average='macro'):.2f}")
print(f"F1-Score: {f1_score(y_test, y_pred_svm, average='macro'):.2f}")

#Validação cruzada para decision tree
dt_cv_scores = cross_val_score(dt_model, X, y, cv=5)
print(f"Acurácia média com K-Fold (Decision Tree): {dt_cv_scores.mean():.2f}")

#validação cruzada para SVM
svm_cv_scores = cross_val_score(svm_model, X, y, cv=5)
print(f"Acurácia média com K-Fold (SVM): {svm_cv_scores.mean():.2f}")
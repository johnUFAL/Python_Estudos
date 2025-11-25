import tensorflow as tf
from tensorflow.keras import layers, models # type: ignore
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# DataSet de digitos
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# Rede neural: 1 input layer, 2 hidden layers e 1 output layer
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax')) # 10 classes pra cada digito

# Definindo f. perda e treino
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))

# Acurácia 
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Acuráci no set de test: {accuracy:.2f}')

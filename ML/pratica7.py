import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models       # type: ignore
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=.2, random_state=42)

# Rede neural com camadas densas: Dropout Batch Normalization
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(.5))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Utilizando f. de parde categorical_crossentropy e otimizando adam
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history =model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))

# Vizualização
plt.plot(history.history['accuracy'], label='Acurácia Treinamento')
plt.plot(history.history['val_accuracy'], label='Acurácia Validação')
plt.xlabel('Épocas')
plt.ylabel('Acurácia')
plt.legend()
plt.title('Acurácia do Modelo durante o Treinamento e Validação')
plt.show()


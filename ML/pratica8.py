import tensorflow as tf
from tensorflow.keras import layers, models # type: ignore
import matplotlib.pyplot as plt
import numpy as np

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train, X_test = X_train / 255.0, X_test / 255.0 # Escalar valores entre 0 e 1

# CNN com duas camadas covulucionais e de pooling
model = models.Sequntial()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Compilação e otimizaçõa do adam e f. perda 
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Verificando métrica
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Acurácia no set de test: {accuracy:.2f}')

# Vizualização
predictions = model.predict(X_test)
for i in range(5):
    plt.imshow(X_test[i], cmap='gray')
    plt.title(f'Previsão: {np.argmax(predictions[i])}')
    plt.show()

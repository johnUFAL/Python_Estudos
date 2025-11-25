import nltk 

def bag_of_words(text, vocabulary):
    tokens = nltk.word_tokenize(text)
    bow = [0]*len(vocabulary)

    for token in tokens:
        if token in vocabulary:
            bow[vocabulary[token]] = 1

    return bow

vocabulary = {
    "gato": 0,
    "cachorro": 1,
    "bola": 2,
    "bicicleta": 3,
    "Azul": 4,
    "Bandeira": 5,
    "carro": 6,
    "viagem": 7
}

text = "O gato e o cachorro são bons mamiferos para levar em viagens de carro."
bow = bag_of_words(text, vocabulary)

print("\nResultado...")
print(bow)
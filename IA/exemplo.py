# Importação de biblioteca(s)
import nltk
from nltk.corpus import treebank
# Pode ser necessário baixar pacotes adicionais da biblioteca NLTK
# nltk.download()
# Texto a ser trabalhado
texto = 'Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.'
print('\nTexto bruto:', texto)
# Fazendo a separação do texto por pontos
print('\nTexto separado:', texto.split('.'))
# Dividindo o texto em frases. Aqui o algoritmo já identifica o texto em duas frases
frase = nltk.tokenize.sent_tokenize(texto)
print('\nIdentificação do número de frases:', frase)
# Dividindo o texto em "tokens" ou palavras - tokenização
token = nltk.word_tokenize(texto.lower())
print('\nImpressão dos tokens:', token)
# Divisão dos tokens em classes com identificação sintática e semântica
classes_token = nltk.pos_tag(token)
print('\nImpressão dos tokens (Pos-Tagging - Part-of-Speech Taggin no formato PennTreeBank):', classes_token)
# Detecção de entidades - agrupamento de tokens em unidades sintáticas
entidades = nltk.chunk.ne_chunk(classes_token)
print('\nImpressão das entidades (Chunking):', entidades)
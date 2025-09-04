from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans

# 1. Dataset
frases = [
    # exemplo: "Quero reservar hotel", ...
    "Posso pagar as passagens com milhas?",
    "A hospedagem é paga no final da viagem?",
    "Quantos passeios são ao todo?",
    "Os restaurantes são perto da orla?"
]

categorias = [
    "passagens", "hospedagem", "passeios", "restaurantes"
]

# 2. Vetorização
modelo = Pipeline([
    ('vetorizacao', CountVectorizer()),
    ('classificador', MultinomialNB())
])

# 3. Modelo
modelo.fit(frases, categorias)

# 4. Previsão
entrada = input("Digite uma frase para o chatbot: ")
saida = modelo.predict([entrada])
print(f"Categoria prevista: {saida[0]}")
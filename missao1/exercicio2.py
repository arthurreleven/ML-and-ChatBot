from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# 1. Dataset
frases = [
    # exemplo: "Quando abre matrícula?", ...
    "Qual o número da minha matrícula?",
    "As notas são calculadas por média aritmética?",
    "Os eventos são ao vivo?",
    "Pode comer na biblioteca?"
]
rotulos = [
    # exemplo: "matricula", ...
    "matricula", "notas", "eventos", "biblioteca"
]

# 2. Vetorização
modelo = Pipeline([
    ('vetorizacao', CountVectorizer()),
    ('classificador', MultinomialNB())
])

# 3. Modelo
modelo.fit(frases, rotulos)

# 4. Previsão
entrada = input("Digite uma frase para o chatbot: ")
saida = modelo.predict([entrada])
print(f"Categoria prevista: {saida[0]}")
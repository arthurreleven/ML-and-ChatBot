'''
Integrantes:
Arthur Luiz da Silva - 93729
Guilherme Castro Pires - 107802
Lucas David Pereira Esteves - 98326
Marcelo Henrique da Silva Nunes - 82893
Otávio Henrique de Souza Silva - 102226
Pedro Henrique Carvilhe Silva - 8121
Victor Vicente - 

Navegue pelos exercícios dessa forma: Exercício 1, Exercício 2, Exercício 3...
'''

#Exercício 1
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Função de pré-processamento
def limpar_texto(texto):
    texto = texto.lower()  # Converte para minúsculas
    texto = re.sub(r'[^\w\s]', '', texto)  # Remove pontuação
    texto = re.sub(r'\d+', '', texto)  # Remove números
    texto = texto.strip()  # Remove espaços extras
    return texto

# 1. Conjunto de dados (mensagens + rótulos)
mensagens = [
    #Info da Loja
    "Qual é o horário de funcionamento da loja?",
    "Onde fica localizada a loja física mais próxima?",
    "Quais são os canais oficiais de atendimento da loja?",
    "Vocês têm alguma política de troca e devolução?"
    
    #Sup
    "Como faço para abrir um chamado de suporte?",
    "Quanto tempo demora para responderem minha solicitação?",
    "Posso falar com um atendente ao vivo?",
    "Quais são os horários de atendimento do suporte?",
    
    #Checkout
    "Por que meu pagamento não foi aprovado no checkout?",
    "Posso salvar meus dados para facilitar futuras compras?",
    "Como aplico um código promocional no checkout?",
    "É possível alterar o pedido depois de finalizar o checkout?",
    
    #Frete
    "Qual o prazo de entrega para o meu CEP?",
    "Tem frete grátis para compras acima de determinado valor?",
    "Posso escolher uma transportadora diferente para a entrega?",
    "Meu pedido está atrasado, como posso acompanhar a entrega?"
]
rotulos = ["Info da Loja", "Info da Loja", "Info da Loja", "Info da Loja",
           "Sup", "Sup", "Sup", "Sup",
           "Checkout", "Checkout", "Checkout", "Checkout",
           "Frete", "Frete", "Frete", "Frete"]


modelo = Pipeline([
    ('vetorizacao', CountVectorizer()),
    ('classificador', MultinomialNB())
])

modelo.fit(mensagens, rotulos)

entrada = input("Digite uma frase para o chatbot: ")
saida = modelo.predict([entrada])
print(f"Categoria prevista: {saida[0]}")

#Exercício 2
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

#Exercício 3
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np

print("\n--- 1.2 Exercício para Alunos (Supervisionado) ---")

# Dados de Treino: [distancia_km, numero_de_pizzas]
dados_entregas = np.array([
    [5, 2],   # 5 km, 2 pizzas
    [2, 1],   # 2 km, 1 pizza
    [10, 4],  # 10 km, 4 pizzas
    [7, 3],   # 7 km, 3 pizzas
    [1, 1]    # 1 km, 1 pizza
])

# Rótulos: Tempo de entrega em minutos
tempos_entrega = np.array([30, 15, 55, 40, 10])

# TODO: Crie uma instância do modelo LinearRegression.
modelo_entrega = LinearRegression()

# TODO: Treine o modelo usando os dados de entregas e os tempos.
modelo_entrega.fit(dados_entregas, tempos_entrega)

# TODO: Faça a previsão para um novo pedido: 8 km de distância e 2 pizzas.
pedido_novo = np.array([[10, 1]])
tempo_previsto = modelo_entrega.predict(pedido_novo)

# print(f"Tempo de entrega previsto para o novo pedido: {tempo_previsto[0]:.2f} minutos")
print(f"SOLUÇÃO: Tempo de entrega previsto para o novo pedido: {tempo_previsto[0]:.2f} minutos")

#Exercício 4
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

# 1. Matriz de mensagens (sem rótulos)
mensagens = [
    "Quero pedir pizza",
    "Qual o valor da pizza grande?",
    "Preciso de suporte no aplicativo",
    "O app está travando",
    "Vocês têm sobremesas?",
    "Meu pedido está atrasado"
]

# 2. Vetorizar texto
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(mensagens)

# 3. Criar modelo de agrupamento
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)

# 4. Mostrar os grupos encontrados
print("\nAgrupamento de mensagens:")
for i, msg in enumerate(mensagens):
    print(f"'{msg}' => Cluster {kmeans.labels_[i]}")

# 5. Interação: classificar nova frase
while True:
    nova_mensagem = input("\nDigite uma nova mensagem (ou 'sair' para encerrar): ")
    if nova_mensagem.lower() == "sair":
        break
    X_novo = vectorizer.transform([nova_mensagem])
    cluster_previsto = kmeans.predict(X_novo)
    print(f"Essa mensagem se parece com o Cluster {cluster_previsto[0]}")

#Exercício 5
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

#Exercício 6
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

print("\n--- Exercício Não Supervisionado ---")

# Dados: [preco_produto, nota_de_popularidade (0-10)]
dados_produtos = np.array([
    [10, 2], [15, 3], [12, 1],   # Categoria 1: Baratos e menos populares
    [200, 9], [180, 8], [210, 10] # Categoria 2: Caros e muito populares
])

# TODO: Crie um modelo KMeans para encontrar 2 clusters.
modelo_produtos = KMeans(n_clusters=2, random_state=42, n_init=10)

# TODO: Treine o modelo com os dados dos produtos.
modelo_produtos.fit(dados_produtos)

# Os centros dos clusters são os nossos produtos "âncora" ideais.
produtos_ancora = modelo_produtos.cluster_centers_

# print(f"Características dos Produtos Âncora (Preço, Popularidade):\n{produtos_ancora}")
print(f"SOLUÇÃO: Características dos Produtos Âncora (Preço, Popularidade):\n{produtos_ancora}")

clusters = ['Cluster 0', "Cluster 1"]
precos = produtos_ancora[:, 0]
plt.title('Produtos Âncora')
plt.xlabel('Clusters')
plt.ylabel('Preços')
plt.bar(clusters, precos, color='r', label=f'(Total: {precos})')
plt.show()
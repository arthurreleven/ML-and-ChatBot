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
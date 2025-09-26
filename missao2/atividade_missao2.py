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
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

print("--- Exercício 1 -  Missão 2 (Aprendizado Supervisionado) ---")

# Dados: [nota_prova_1, nota_trabalho_2]
# Rótulos: 0 = Reprovou, 1 = Passou
# Cloque notas no seu DataSet
X_treino = np.array([
    [2, 9], [3, 6], [3, 7], [2, 8], # Passou
    [0, 1], [0, 2], [1, 1], [1, 4]  # Reprovou
])
y_treino = np.array([1, 1, 1, 1, 0, 0, 0, 0])

# Criando o modelo. O KNN decide o rótulo de um novo ponto olhando para seus vizinhos mais próximos.
# n_neighbors=3 significa que ele vai consultar os 3 vizinhos mais próximos.
modelo_knn = KNeighborsClassifier(n_neighbors=3)

# O '.fit()' é onúcleo do aprendizado: o modelo analisa os dados e ajusta seus parâmetros.
modelo_knn.fit(X_treino, y_treino)

# testar com novos alunos.
aluno_A = np.array([[1, 2]]) # Esperamos que passe (1)
aluno_B = np.array([[2, 9]]) # Esperamos que reprove (0)

# O '.predict()' usa o conhecimento adquirido para fazer uma previsão.
previsao_A = modelo_knn.predict(aluno_A)
previsao_B = modelo_knn.predict(aluno_B)

print(f"Dados de treino (Notas): \n{X_treino}")
print(f"Rótulos de treino (Situação): {y_treino}")
print("-" * 20)
print(f"Previsão para o Aluno A: {'Passou' if previsao_A[0] == 1 else 'Reprovou'}")
print(f"Previsão para o Aluno B: {'Passou' if previsao_B[0] == 1 else 'Reprovou'}")
print("-" * 50, "\n")

#Exercício 2
from sklearn.linear_model import LinearRegression
import numpy as np

print("--- Exercício 2 -  Missão 2 (Aprendizado Supervisionado) ---")

# Dados: [área_m2, numero_quartos]
# Rótulos: preco_em_milhares_de_reais
X_imoveis = np.array([
    [60, 2], [75, 3], [80, 3], # Imóveis menores
    [120, 3], [150, 4], [200, 4] # Imóveis maiores
])
y_precos = np.array([150, 200, 230, 310, 400, 500])

# TODO: Crie uma instância do modelo LinearRegression.
modelo_regressao = LinearRegression()

# TODO: Treine o modelo com os dados de imóveis (X_imoveis, y_precos).
modelo_regressao.fit(X_imoveis,y_precos)

# TODO: Crie um novo imóvel para testar (ex: 100m², 3 quartos).
imovel_teste = np.array([[100, 3]])

# TODO: Faça a previsão do preço para o novo imóvel.
preco_previsto = modelo_regressao.predict(imovel_teste)

# print(f"Previsão de preço para um imóvel de 100m² com 3 quartos: R$ {preco_previsto[0]:.2f} mil")
print("Complete o código acima!")
print("-" * 50, "\n")
print(f"Previsão de preço para um imóvel de 100m² com 3 quartos: R$ {preco_previsto[0]:.2f} mil")

#Exercício 3
from sklearn.cluster import KMeans
import numpy as np

print("--- Exercício 3 -  Missão 2 (Aprendizado Supervisionado) ---")

# Dados: [valor_gasto_medio, frequencia_visitas_mensal]
# Não temos rótulos!
clientes = np.array([
    [30, 1], [45, 2], [35, 1], # Grupo de baixo valor/frequência
    [500, 8], [600, 10], [550, 9] # Grupo de alto valor/frequência
])

# Criamos o modelo KMeans e pedimos para ele encontrar 2 clusters. Parametrize da forma que seja melhor (ver outros exemplos)
kmeans = KMeans(n_clusters = 2, random_state = None, n_init = 15)

# '.fit_predict()' treina o modelo e já retorna o cluster de cada cliente.
clusters_encontrados = kmeans.fit_predict(clientes)

print(f"Dados dos clientes (sem rótulos):\n{clientes}")
print(f"Clusters encontrados pelo KMeans para cada cliente: {clusters_encontrados}")
print("Observe como o algoritmo separou corretamente os clientes nos grupos 0 e 1.")
print("-" * 50, "\n")

#Exercício 4
from sklearn.cluster import KMeans
import numpy as np

print("--- Exercício 4 -  Missão 2 (Aprendizado Não Supervisionado) ---")

# Dados: [valor_transacao, hora_do_dia (0-23)]
transacoes = np.array([
    [15.50, 14], [30.00, 10], [12.75, 11],
    [50.20, 19], [25.00, 9],
    [2500.00, 3] # Uma transação muito alta e de madrugada -> suspeita
])

# TODO: Crie um modelo KMeans para encontrar 2 grupos.
# A ideia é que as transações normais fiquem em um grupo e a anômala fique sozinha no outro.
modelo_anomalia = KMeans(n_clusters=2, random_state=None, n_init=10)

# TODO: Treine e preveja os clusters para os dados de transações.
clusters_transacoes = modelo_anomalia.fit_predict(transacoes)

# print(f"Clusters para as transações: {clusters_transacoes}")
# print("A transação anômala é aquela que está em um cluster isolado!")
print("-" * 50, "\n")
print(f"Clusters para as transações: {clusters_transacoes}")
print("A transação anômala é aquela que está em um cluster isolado!")

#Exercício 5
import time
# --- CONFIGURAÇÃO DO AMBIENTE ---
POSICAO_INICIAL = 0
POSICAO_COMIDA = 4
recompensa_total = 0

# O agente começa na posição inicial.
posicao_agente = POSICAO_INICIAL

print("--- Iniciando a Simulação do PERSONAGEM COMILÃO ---")
print(f"O agente começa na posição {posicao_agente} e quer chegar na comida na posição {POSICAO_COMIDA}.")
print("-" * 30)

# O agente tem no máximo 10 passos para tentar chegar à comida.
for passo in range(10):
    print(f"Passo {passo + 1}:")
    
# O agente sempre toma a mesma AÇÃO: mover para a 'direita'.
    acao_agente = 'direita'
    print(f"   -> Ação do Agente: '{acao_agente}'")

# 1. ATUALIZE A POSIÇÃO DO AGENTE
    #    Como a ação é sempre 'direita', simplesmente incrementamos a posição.
    posicao_agente = posicao_agente + 1
        
# 2. CALCULE A RECOMPENSA DO PASSO
#    Verificamos primeiro a condição de vitória.
    if posicao_agente == POSICAO_COMIDA:
        # Se chegou, recebe a recompensa positiva.
        recompensa_do_passo = 20
    else:
        # Se ainda não chegou, recebe a penalidade de movimento.
        recompensa_do_passo = -1

# 3. ATUALIZE A RECOMPENSA TOTAL
#    Acumulamos a recompensa do passo na variável total.
    recompensa_total = recompensa_total + recompensa_do_passo
        
# Exibe o resultado do passo
    print(f"   <- Resposta do Ambiente: Nova Posição={posicao_agente}, Recompensa={recompensa_do_passo}")
        
# 4. VERIFIQUE SE O JOGO TERMINOU
#    Se a condição de vitória foi atingida, paramos a simulação.
    if posicao_agente == POSICAO_COMIDA:
        print("\nO personagem encontrou a comida!")
        break
        
# Pausa para visualização
    time.sleep(1)

print("-" * 30)
print(f"Simulação Finalizada! Recompensa total acumulada: {recompensa_total}")
# Resultado esperado: O agente leva 4 passos, acumulando -4 de recompensa. No 4º passo, ele alcança a comida e ganha +20. Recompensa total: (-1 * 3) + 20 = 17. Não, espera.
# Passo 1: pos=1, rec=-1, total=-1
# Passo 2: pos=2, rec=-1, total=-2
# Passo 3: pos=3, rec=-1, total=-3
# Passo 4: pos=4, rec=+20, total=17
# O resultado esperado é 17.
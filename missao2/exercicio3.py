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
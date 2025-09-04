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
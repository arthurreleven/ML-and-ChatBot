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
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Suponha que estas variáveis já existem e foram geradas pelo código anterior
# --- Início do Bloco de Contexto (não precisa alterar) ---
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

dados = {
    'tamanho_m2': [50, 70, 100, 120, 65, np.nan, 95, 88, 110, 150],
    'n_quartos': [1, 2, 3, 3, 2, 2, 3, 2, 3, 4],
    'cidade': ['SP', 'RJ', 'SP', 'BH', 'RJ', 'SP', 'BH', 'RJ', 'SP', 'BH'],
    'preco': [150000, 210000, 300000, 350000, 190000, 180000, 280000, 250000, 320000, 450000]
}
df = pd.DataFrame(dados)
imputer = SimpleImputer(strategy='mean')
df['tamanho_m2'] = imputer.fit_transform(df[['tamanho_m2']])
X = df.drop('preco', axis=1)
y = df['preco']
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)
colunas_numericas = ['tamanho_m2', 'n_quartos']
colunas_categoricas = ['cidade']
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
X_treino_cat = encoder.fit_transform(X_treino[colunas_categoricas])
X_teste_cat = encoder.transform(X_teste[colunas_categoricas])
scaler = StandardScaler()
X_treino_num = scaler.fit_transform(X_treino[colunas_numericas])
X_teste_num = scaler.transform(X_teste[colunas_numericas])
X_treino_final = np.hstack([X_treino_num, X_treino_cat])
X_teste_final = np.hstack([X_teste_num, X_teste_cat])

# --- INÍCIO DO SEU TRABALHO
# 1. Crie uma instância do modelo de Regressão Linear

modelo_preco_casas = LinearRegression()

# 2. Treine o modelo com os dados de TREINO. Use o método .fit() com os dados de treino (X_treino_final e y_treino).
modelo_preco_casas.fit(X_treino_final, y_treino)

print("Modelo treinado com sucesso!")

# 3. Faça previsões nos dados de TESTE. Use o método .predict() no conjunto de teste (X_teste_final).
previsoes = modelo_preco_casas.predict(X_teste_final)

print("\n--- Resultados da Avaliação ---")
# Vamos comparar as previsões com os valores reais (y_teste)
for i in range(len(previsoes)):
    print(f"Imóvel {i+1}: Preço Real = R${y_teste.iloc[i]:.2f} | Previsão do Modelo = R${previsoes[i]:.2f}")

# 4. Avalie a performance do modelo
# Usaremos duas métricas:
# - Erro Absoluto Médio (MAE): A média da diferença (em R$) entre o preço real e a previsão. Quanto menor, melhor.
# - R² Score: Indica o quão bem o modelo explica a variação dos dados. Varia de 0 a 1. Quanto mais perto de 1, melhor.

# Dica: Use as funções mean_absolute_error() e r2_score(). Elas recebem (y_teste, previsoes) como argumentos.
mae = mean_absolute_error(y_teste, previsoes)
r2 = r2_score(y_teste, previsoes)

print(f"\nErro Absoluto Médio (MAE): R$ {mae:.2f}")
print(f"Score R²: {r2:.2f}")
# --- FIM DO SEU TRABALHO ---

#Exercício 2
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# --- 2. DATASET (Grande e com desafios reais) ---
# Dataset simulado de carros usados
data = {
    'Ano': [2018, 2015, 2019, 2020, 2017, 2014, 2018, 2016, 2021, 2013, 2019, 2017, 2015, 2020, 2018, 2016, 2022, 2014, 2019, 2017],
    'Quilometragem': [50000, 120000, 30000, 15000, 70000, 150000, 60000, 95000, 5000, 180000, 40000, 80000, 110000, 20000, 55000, 105000, 2000, 160000, 35000, 75000],
    'Potencia_Motor': [1.6, 2.0, 1.0, 1.4, 1.8, 2.0, 1.6, 1.8, 1.0, 2.2, 1.4, 1.6, 2.0, 1.0, 1.8, 2.0, 1.2, 2.2, 1.4, 1.8],
    'Tipo_Combustivel': ['Flex', 'Gasolina', 'Flex', 'Flex', 'Gasolina', 'Diesel', 'Flex', 'Gasolina', 'Flex', 'Diesel', 'Flex', 'Flex', 'Gasolina', 'Flex', 'Gasolina', 'Diesel', 'Flex', 'Diesel', 'Flex', 'Gasolina'],
    'Cambio': ['Manual', 'Automatico', 'Manual', 'Manual', 'Automatico', 'Manual', 'Automatico', 'Automatico', 'Manual', 'Automatico', 'Manual', 'Manual', 'Automatico', 'Manual', 'Automatico', 'Automatico', 'Manual', 'Automatico', 'Manual', 'Automatico'],
    'Preco': [45000, 38000, 55000, 65000, 52000, 35000, 48000, 46000, 75000, 32000, 58000, 50000, 40000, 68000, 53000, 44000, 82000, 30000, 60000, 51000]
}
df_carros = pd.DataFrame(data)

# Adicionando valores ausentes para o desafio
df_carros.loc[5, 'Quilometragem'] = np.nan
df_carros.loc[11, 'Potencia_Motor'] = np.nan

print("--- Análise Inicial: Dataset de Carros ---")
df_carros.info()
print("\nValores ausentes:")
print(df_carros.isnull().sum())

# --- INÍCIO DO TRABALHO ---
# --- 3. PREPARAÇÃO DOS DADOS ---
# 3.1. Separe as features (X) do alvo (y)
# Dica: 'y' é a coluna 'Preco'. 'X' são todas as outras.

X = df_carros.drop('Preco', axis=1)
y = df_carros['Preco']

# 3.2. Divida os dados em conjuntos de treino e teste
# Dica: Use 20% para teste e random_state=42 para consistência.
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.20, random_state=22)

# 3.3. Crie um pipeline de pré-processamento
# Dica: Use ColumnTransformer para aplicar transformações diferentes em colunas diferentes.
# Para colunas numéricas: um SimpleImputer (para preencher NaN) e um StandardScaler.
# Para colunas categóricas: um OneHotEncoder.

colunas_numericas = ['Ano', 'Quilometragem', 'Potencia_Motor']
colunas_categoricas = ['Tipo_Combustivel', 'Cambio']

# Pipeline para dados numéricos
pipeline_numerico = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Pipeline para dados categóricos
pipeline_categorico = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Junte os pipelines em um ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', pipeline_numerico, colunas_numericas),
        ('cat', pipeline_categorico, colunas_categoricas)
    ])

# --- 4. TREINAMENTO DO MODELO ---
# 4.1. Crie o modelo de Regressão Linear
modelo_reg = LinearRegression()

# 4.2. Crie o pipeline final que une o pré-processador e o modelo
# Dica: Este pipeline fará todo o trabalho: pré-processar e depois treinar.
pipeline_final_reg = Pipeline(steps=[('preprocessor', preprocessor),
                                     ('regressor', modelo_reg)])

# 4.3. Treine o pipeline completo com os dados de treino
# Dica: Use o método .fit() no pipeline final com X_treino e y_treino.
pipeline_final_reg.fit(X_treino, y_treino)

print("\n Modelo de Regressão treinado com sucesso!")

# --- 5. AVALIAÇÃO DO MODELO ---
# 5.1. Faça previsões com os dados de teste
# Dica: Use o método .predict() no pipeline treinado com X_teste.

previsoes_preco = pipeline_final_reg.predict(X_teste)

# 5.2. Calcule as métricas de avaliação
mae = mean_absolute_error(y_teste, previsoes_preco)
r2 = r2_score(y_teste, previsoes_preco)

print("\n--- Resultados da Avaliação (Regressão) ---")
print(f"Erro Absoluto Médio (MAE): R$ {mae:.2f}")
print(f"Score R²: {r2:.2f}")

# 5.3. Visualize os resultados
plt.figure(figsize=(10, 6))
plt.scatter(y_teste, previsoes_preco)
plt.plot([y_teste.min(), y_teste.max()], [y_teste.min(), y_teste.max()], '--r', linewidth=2)
plt.xlabel("Preços Reais")
plt.ylabel("Preços Previstos")
plt.title("Preços Reais vs. Previsões do Modelo de Regressão")
plt.show()

#Exercício 3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# --- 2. DATASET ---
data = {
    'Idade': [25, 45, 35, 50, 22, 55, 41, 28, 33, 60, 39, 48, 29, 52, 31, 65, 27, 38, 43, 58],
    'Plano_Mensal': [70, 95, 80, 105, 50, 110, 90, 65, 75, 115, 85, 100, 72, 108, 78, 120, 68, 82, 92, 112],
    'Meses_Contrato': [1, 24, 12, 36, 2, 48, 18, 5, 8, 60, 15, 30, 3, 40, 6, 55, 4, 10, 22, 50],
    'Tipo_Contrato': ['Mensal', 'Anual', 'Mensal', 'Dois anos', 'Mensal', 'Dois anos', 'Anual', 'Mensal', 'Mensal', 'Dois anos',
                      'Anual', 'Dois anos', 'Mensal', 'Dois anos', 'Mensal', 'Dois anos', 'Mensal', 'Anual', 'Anual', 'Dois anos'],
    'Suporte_Tecnico': ['Sim', 'Nao', 'Sim', 'Nao', 'Nao', 'Nao', 'Sim', 'Sim', 'Nao', 'Nao',
                        'Sim', 'Nao', 'Sim', 'Nao', 'Sim', 'Nao', 'Sim', 'Sim', 'Nao', 'Nao'],
    'Churn': ['Sim', 'Nao', 'Sim', 'Nao', 'Sim', 'Nao', 'Nao', 'Sim', 'Sim', 'Nao',
              'Nao', 'Nao', 'Sim', 'Nao', 'Sim', 'Nao', 'Sim', 'Nao', 'Nao', 'Nao']
}
df_churn = pd.DataFrame(data)

# Adicionando valores ausentes
df_churn.loc[3, 'Plano_Mensal'] = np.nan

print("--- Análise Inicial: Dataset de Churn ---")
df_churn.info()
print("\nValores ausentes:")
print(df_churn.isnull().sum())

# --- 3. PREPARAÇÃO DOS DADOS ---
# 3.1. Separe as features (X) do alvo (y)
X = df_churn.drop('Churn', axis=1)
y = df_churn['Churn']

# 3.2. Divida os dados em conjuntos de treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.25, random_state=42)

# 3.3. Crie um pipeline de pré-processamento
colunas_numericas = ['Idade', 'Plano_Mensal', 'Meses_Contrato']
colunas_categoricas = ['Tipo_Contrato', 'Suporte_Tecnico']

pipeline_numerico = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

pipeline_categorico = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', pipeline_numerico, colunas_numericas),
        ('cat', pipeline_categorico, colunas_categoricas)
    ])

# --- 4. TREINAMENTO DO MODELO ---
modelo_cla = LogisticRegression()

pipeline_final_cla = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', modelo_cla)
])

pipeline_final_cla.fit(X_treino, y_treino)
print("\nModelo de Classificação treinado com sucesso!")

# --- 5. AVALIAÇÃO DO MODELO ---
previsoes_churn = pipeline_final_cla.predict(X_teste)

acuracia = accuracy_score(y_teste, previsoes_churn)
relatorio = classification_report(y_teste, previsoes_churn)
matriz_conf = confusion_matrix(y_teste, previsoes_churn)

print("\n--- Resultados da Avaliação (Classificação) ---")
print(f"Acurácia: {acuracia*100:.2f}%")
print("\nRelatório de Classificação:")
print(relatorio)

plt.figure(figsize=(8, 6))
sns.heatmap(matriz_conf, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Nao Churn', 'Churn'], yticklabels=['Nao Churn', 'Churn'])
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()


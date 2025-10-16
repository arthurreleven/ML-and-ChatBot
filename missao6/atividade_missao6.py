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
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

#Dataset dos dados de remuneração
data = {
  'idades': [25, 30, 35, 40, 45, 50, 55, 60, 65],
  'salario_anual': [42000, 45000, 56000, 64000, 67000, 90000, 115000, 135000, 142000],
  'anos_empregados': [0, 2, 5, 7, 12, 14, 19, 25, 30],
  'valor_emprestimo': [5000, 10000, 20000, 30000, 40000, 50000, 60000, 90000, 100000],
  'tipo_moradia': ["aluguel", "propria", "financiada", "aluguel", "propria", "financiada", "aluguel", "propria", "financiada"],
  'risco_inadimplencia': [0, 1, 0, 1, 0, 1, 0, 1, 0]
}

data_pd = pd.DataFrame(data)

#Preparação das features
X = data_pd.drop('risco_inadimplencia', axis=1)
y = data_pd['risco_inadimplencia']

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=10)

#Pipeline Pré-Processamento
col_numericas = ['idades', 'salario_anual', 'anos_empregados', 'valor_emprestimo']
col_categoricas = ['tipo_moradia']

# Pipeline para dados numéricos
pipeline_numerico = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Pipeline para dados categóricos
pipeline_categorico = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

#Pré-Processador com ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
  ('num', pipeline_numerico, col_numericas),
  ('cat', pipeline_categorico, col_categoricas)
])

#Modelo
modelo = LogisticRegression() 

#Pipeline Final
pipeline_final_pre = Pipeline(steps=[
  ('preprocessor', preprocessor),
  ('modelo', modelo)
])

#.fit
pipeline_final_fit = pipeline_final_pre.fit(X_treino, y_treino)

print("\n Modelo treinado com sucesso!")

# Avaliando
y_pred = pipeline_final_pre.predict(X_teste)
print("\nAcurácia:", accuracy_score(y_teste, y_pred))
print("\nRelatório de Classificação:\n", classification_report(y_teste, y_pred))
print("\nPontuação ROC AUC:", roc_auc_score(y_teste, pipeline_final_pre.predict_proba(X_teste)[:,1]))

#Exercício 2
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# ====== 1. Criar Dataset Simulado ======
# Criando datas
datas = pd.date_range(start='2025-01-01', end='2025-03-31', freq='D')

# Criando features
temperatura_media = np.random.randint(0, 36, len(datas))
dia_util = [1 if d.weekday() < 5 else 0 for d in datas]  # 1=dia útil, 0=fim de semana

# Criando alvo com uma relação simples (quanto mais frio ou fim de semana, menor consumo)
consumo_energia_kwh = 2000 + temperatura_media*50 + np.array(dia_util)*500 + np.random.randint(-200, 201, len(datas))

# Criando DataFrame
df = pd.DataFrame({
    'data': datas,
    'temperatura_media': temperatura_media,
    'dia_util': dia_util,
    'consumo_energia_kwh': consumo_energia_kwh
})

# ====== 2. Engenharia de Atributos ======
df['mes'] = df['data'].dt.month
df['dia_da_semana'] = df['data'].dt.dayofweek
df['dia_do_ano'] = df['data'].dt.dayofyear
df = df.drop(columns='data')  

# ====== 3. Separar X e y ======
X = df.drop(columns='consumo_energia_kwh')
y = df['consumo_energia_kwh']

# ====== 4. Divisão treino/teste ======
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ====== 5. Criar Pipeline ======
pipeline = Pipeline([
    ('scaler', StandardScaler()), 
    ('rf', RandomForestRegressor(n_estimators=100, random_state=42))
])

# ====== 6. Treinamento ======
pipeline.fit(X_train, y_train)

# ====== 7. Avaliação ======
y_pred = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae:.2f} kWh')
print(f'R² Score: {r2:.2f}')

# ====== 8. Visualizar  previsões ======
resultados = pd.DataFrame({
    'Real': y_test,
    'Previsto': y_pred
})
print(resultados.head(10))

#Exercício 3
import pandas as pd

dados = {
    'texto': [
        "oferta imperdível clique aqui agora",
        "ganhe dinheiro fácil",
        "relatório de vendas anexo",
        "oi, tudo bem? reunião amanhã",
        "clique e ganhe prêmio",
        "almoço hoje no restaurante",
        "promoção especial só hoje",
        "encontro marcado para reunião",
    ],
    'categoria': ['spam', 'spam', 'ham', 'ham', 'spam', 'ham', 'spam', 'ham']
}

df = pd.DataFrame(dados)

# Importação para dividir os dados em treino e teste
from sklearn.model_selection import train_test_split

# 2. Separar X e y e dividir em treino e teste
X = df['texto']
y = df['categoria']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Importações para pipeline, vetorização e classificação
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# 3. Criar o pipeline com TfidfVectorizer e MultinomialNB
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),   
    ('clf', MultinomialNB())        
])

# 4. Treinar o modelo
pipeline.fit(X_train, y_train)

# Importações para avaliação
from sklearn.metrics import classification_report, accuracy_score

# 5. Fazer previsões e avaliar o modelo
y_pred = pipeline.predict(X_test)

print("Acurácia:", accuracy_score(y_test, y_pred))
print("\nRelatório de classificação:\n", classification_report(y_test, y_pred))

#Exercício 4
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


iris = load_iris()
X = iris.data       
y = iris.target      


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5))  
])

pipeline.fit(X_train, y_train)



y_pred = pipeline.predict(X_test)


acc = accuracy_score(y_test, y_pred)
print(f'Acurácia: {acc:.2f}')


print(classification_report(y_test, y_pred, target_names=iris.target_names))

#Exercício 5
# 1. Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, r2_score

# 2. Carregar o dataset (com sep=';' pois os dados usam ponto e vírgula)
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
df = pd.read_csv(url, sep=';')

# 3. Separar features (X) e alvo (y)
X = df.drop('quality', axis=1)
y = df['quality']

# 4. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# 5. Criar pipeline com scaler + SVR
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svr', SVR())  # Usa os parâmetros padrão
])

# 6. Treinar o modelo
pipeline.fit(X_train, y_train)

# 7. Fazer previsões e avaliar
y_pred = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE (Erro Médio Absoluto): {mae:.2f}")
print(f"R² Score: {r2:.2f}")

# Visualização de dados em Python
# Matplotlib
# Pandas
# Seaborn

# Matplotlib
# Desempenha papel centro em criação de gráfico.
import matplotlib.pyplot as plt
import random

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)
print(dados1)
print(dados2)
plt.plot(dados1, dados2)

# Pandas
# As principais estruturas (Series e DataFrame) possuem o método plot() que permite criar gráficos a partir dos dados
import pandas as pd
dados = {
    'Produto' : ['A', 'B', 'C'],
    'qtde_vendida' : [33, 50, 45]
}

df = pd.DataFrame(dados)
df.plot(x='Produto', y='qted_vendida', kind='bar')
df.plot(x='Produto', y='qted_vendida', kind='pie')
df.plot(x='Produto', y='qted_vendida', kind='line')


# Biblioteca Seaborn
# Construída sobre base do Matplotlib, destaca-se na criação de gráficos de forma especializada
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='whitegrid') # DataFrame de exemplo

df_tips = sns.load_dataset('tips')
print(df_tips)

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0]) # media por sexo

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
# O motivo pelo barplot() muitas vezes se baseia nos parâmetros adicionais e na flexibilidade que ele oferece. Destacamos o estimator que por padrao calcula a media

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)
# a função barplot oferece uma variedade de opções de estastítica, permitindo a escolha métrica que melhor encaixa nos objetivos. Você pode calcular a soma, contagem ou métricas personalizadas


# Exercício: suponha que você precise responder qual período que os clientes gastam mais no restaurante e se esse período é o que eles dão mais gorjetas.
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='whitegrid')
df = sns.load_dataset('tips')

plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df, estimator=sum, ci=None, palette="Set2")
plt.xlabel("Período (Time)")
plt.ylabel("Total de Gastos")
plt.ylabel("Total de Gastos por Período (Almoço ou Jantar)")
plt.show()


plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df)
plt.xlabel("Período (Time)")
plt.ylabel("Média de Gorjeta")
plt.ylabel("Média de Gorjeta por Período (Almoço ou Jantar)")
plt.show()


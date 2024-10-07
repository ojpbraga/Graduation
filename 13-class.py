# Manipulação de dados
# Métodos de leitura e escrita da biblioteca Pandas: csv, json, html, latex, xml, ms excel etc. Dados binários também são possíveis de leitura.

# Capturar e transformar dados

import pandas as pd
df_selic = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')
print(df_selic.info())
print(df_selic)

# Verificar duplicidade de linhas (IMPORTANTE), utilizando drop_duplicates()
df_selic.drop_duplicates(keep='last', inplace=True)
# Mantém o último registro (keep='lest')
# através do parâmetro inplace="True", faz com que a transformação seja salva do DataFrame.

# Adicionando Colunas
from datetime import date
from datetime import datetime as dt

data_extracao = date.today()

df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Arlei"
print(df_selic.info())
df_selic.head(5) # Mostra o cabeçalho com a qtd que quer

# Buscar Informações
df_selic[0] #localiza index 0
df_selic[[10, 20, 30]] # traz o três itens


# Exemplo: quero saber a taxa da Selic abaixo de x 
teste = df_selic['valor'] < 0.01
print(type(teste)) # É do tipo Serie
print(teste) # A resposta é True ou False

# Exercício
# Suponha que você trabalhe em uma loja em que vende itens variados. Por conta de um erro do sistema, não é mostrado o valor unitário dos itens vendidos e existem algumas duplicações de linhas. Você precisa mostrar itens com valores acima de 50

import pandas as pd

# Criando um DataFrame com 5 linhas de código
data = {
    'nome' : ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto E'],
    'quantidade' : [3, 1, 4, 3, 2],
    'tipo' : ['Eletrônimo', 'Vesturário', 'Alimento', 'Eletrônico', 'Alimento'],
    'receita' : [120, 80, 120, 90]
}
df = pd.DataFrame(data)
print(df)

# Duplicando uma linha
df.drop_duplicates(keep='lest', inplace=True)
print(df)

# Calculando a coluna 'preco'
df['preco'] = df['receita'] / df['quantidade']

# Selecionando itens acima de 50
itens_acima_50 = df[df['preco'] > 50]
print("Itens acima de 50")
print(itens_acima_50)



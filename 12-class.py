# Library Pandas
# This library was created for organize and analysis data more pratic
# Dataframe: structure flexible data, likes table and list
# Manipulation of data: filter, select, order
# Write and read files: cvs, excel, sql, hdf5
# Processing of missing data
# Show data
# integration with NumPy

# Séries: estrutura unidimensional de dados que pode armazenar qualquer tipo de dado
# O principal parâmetro é "data", que pode conter um valor único, uma lista de valores ou um dicionário. Outros parâmetros como "index", "dtype", "name" e outros, têm valores padrão predefinidos, tornando sua especificação opcional.
# Série a partir de uma lista

import pandas as pd

# Creating a list of values
exemple_1 = [10, 20, 30, 40, 50]
print(exemple_1)

# Creating a serie from a list
serie_1 = pd.Series(data = exemple_1)
print(serie_1)

# Creating a dict with key-value pairs
exemple_2 = {'A' : 100, 'B' : 200, 'C' : 300, 'D' : 400, 'E' : 500}
print(exemple_2)

# Creating a serie from a dict
serie_2 = pd.Series(data = exemple_2)
print(serie_2)

# Reading sctucture data with the Pandas library
# Pandas can read data and store in a dataframe
# pandas.read_xxxx or pd.read_xxxx
# Using pandas.read_html() to extract tabels in a site
# url = "https://www.fdic.gov/bank-failures/failed-bank-list"
# result = pd.read_html(url)
# print(type(result))
# print(len(result))

# df_banks = result[0]
# print(df_banks.shape)


# Exercise
data = {
    'name' : ['Alice', 'Bob', 'Eve'],
    'age' : [20, 10, 99]
}
serie_age = pd.Series(data["age"], index=data["name"])
print("Serie Ages:")
print(serie_age)

middle_age = serie_age.mean()
print(f"Middle age: {middle_age}")
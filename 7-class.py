# Estruturas de dados em Python
# Objetos do tipo set (Objetos)
# Um conjunto, ou set, é uma estrutura de dados que represena uma coleção de elementos únicos, sem repetição. Veremos como criar, modificar e realizar operações com conjuntos.

set_exemplo = set()
set_exemplo.add(10)
set_exemplo.add(20)
set_exemplo.add('str')
print(set_exemplo)

set_obj = {10, 20, 'Oi'}
print(type(set_obj))
print(type(set_exemplo))

set_obj.remove(20)
if 20 in set_obj:
    print(True)
else:
    print(False)


# Objetos Mapping
# Dicionários (dict) são estruturas que associam chaves a valores.
dict_exemplo = {'name' : 'Maria', 'age' : 20}
dict_exemplo['license_car'] = True

print(dict_exemplo)
print(dict_exemplo.get('name'))

# Utilizando Tuplas
dict_jonh = dict([('name','Jonh'), ('age', 25)])
print(dict_jonh)

# Utilizando zip para as chaves e outra para valores
dict_gabriel = dict(zip(['name', 'age'], ['Gabriel', 40]))
print(dict_gabriel)

# Verificar se a construção dos objetos são igual
dict_1 = {'name' : 'Maria', 'age' : 20}
dict_2 = {'name' : 'Maria', 'age' : 20}
dict_3 = {'name' : 'Maria', 'age' : 20}
print(dict_1 == dict_2 == dict_3)

# Objetos NumPy
# NumPy é uma biblioteca para computação científica, fornece recursos para manipular array multidimensionais.
import numpy as np

# Criando uma array NumPy
array_numpy = np.array([1, 2, 3, 4, 5])
print(f"Array NumPy original: {array_numpy}")

# Operações matemáticas com array
squared_array = array_numpy ** 2
print(f"Cada elemento elevado ao quadrado: {squared_array}")

sum_of_elements = np.sum(array_numpy)
print(f"Soma de todos os elementos: {sum_of_elements}")

print(f"Acessando index 2: {array_numpy[2]}")

# Exercício
guests = [
    {'name': 'Jonh', 'localization': 'EUA', 'corporation':'EMCORP', 'interest': ['biology']},
    {'name': 'Mariah', 'localization': 'EU', 'corporation':'SUPO', 'interest': ['administration']},
    {'name': 'Kim', 'localization': 'EUA', 'corporation':'YOPU', 'interest': ['biology']}
]

locations = set(guest["localization"] for guest in guests)

corporations = {}
for guest in guests:
    corporation = guest["corporation"]
    if corporation not in corporations:
        corporations[corporation] = []
    corporations[corporation].append(guest["name"])

fields_of_interest = np.array([interest for guest in guests for interest in guest["interest"]])

unique_interest, count = np.unique(fields_of_interest, return_counts=True)

popular_fields_of_interest = unique_interest[np.argmax(count)]

print("Regiões: ", locations)
print("Corporations: ")
for corporations, names in corporations.items():
    print(f"{corporation}, {', '.join(names)}")
print("Area of interest: ", fields_of_interest)
print("Popular area of interest: ", popular_fields_of_interest)
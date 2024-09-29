# Objetos do tipo sequência
# Sequências são estruturas de dados que nos permitem armazenar coleções ordenadas de informações
# Utiliza índice, começa no 0.

# Operações mais comuns:
# x in s: True caso algum item seja igual a x
# s + t: Concatenção de s e t
# n * s: Adiciona s a si mesmo n vezes
# s[i]: Acessa valor da posição i
# s[i:j]: Acessa os valores da posição i até j
# s[i:j:k]: Acessa os valores da posição i até j, com passo k
# len(s): comprimento de s
# min(s): menor valor de s
# max(s): maior valor de s
# s.count(x): número total de ocorrência de x em s

# Lembrando que str é array
text = "Explorando Python"
print(f"Tamanho do texto: {len(text)}")
print(f"Python in text: {'Python' in text}")
print(f"Quantidade de e no texto: {text.count('e')}")
print(f"5 primeiras letras: {text[:5]}")
print(f"Última letra: {text[-1]}")


# Listas
# São formas fundamental de objetos do tipo sequência, são mutáveis, o que significa que podemos adicionar, remover e alterar elementos.

colors = ['yellow', 'green', 'pink']
for cor in colors:
    print(f"For {cor}, position {colors.index(cor)}")

# List comprehensions, Map e Filter
# List comprehensions, ou listcomps, cria listas com base em objetos iteráveis.
# Útil para transformar, filtrar informações de uma sequência existente para criar uma nova sequência com as informações desejadas.

programming_languages = ['Python', 'JavaScript', 'Java', 'Klotin']
print(f"Antes da listcomp {programming_languages}")
programming_languages_comp = [item.lower() for item in programming_languages]
print(f"Depois da listcomp: {programming_languages_comp}")
print("")

# Map
# Aplica a uma função em toda a sequência
# map(funcao, sequencia)
prices_dollars = [100, 50, 75, 120]
taxe_transition = 5.25
prices_brazilian = list(map(lambda x: x * taxe_transition, prices_dollars))
print(prices_brazilian)

# Filter
# Filtra elementos de uma sequência com base em uma função de teste (true or false)
# filter(funcao, sequencia)
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")


# Tupla
# Única diferença das listas: são imutáveis, não pode sobrescrever
# Por exemplo a venda de algo por um valor, esse valor é imutável

tuple1 = ()
tuple2 = ('a', 'b', 'c')
print(f"Type of tuplas: {type(tuple1)}")
for index, value in enumerate(tuple2):
    print(f"Position = {index}, value = {value}")

invited = ('João', 'Eric', 'Ana', 'Alex')
confirmed = ['João', 'Ana']
not_confirmed = [guest for guest in invited if guest not in confirmed]
print(not_confirmed)

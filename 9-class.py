# Módulos e Biblioteca em Python
# São componentes de código que servem como conjuntos de funções em Python que facilitam a organização do código e a reutilização de funções em várias aplicações.

# Principais abordagens para organizar o código: utilizar funções ou encapsular funcionalidades e dividindo o código em vários arquivos

import math
math.sqrt(25)
math.log2(1024)
math.cos(45)

import math as m
m.sqrt(25)

from math import sqrt, log2, cos
sqrt(25)


# Classificação de módulos
# Bibliotecas buil-in (já embutidas)
# math, os, svs, random, datetime, re, collections

# Bibliotecas de terceiros: pesquisar no PyPI
# pip install requests
# Matplotlib é uma biblioteca de visualização, oferece recursos para criar gráficos de dados e, até mesmo, animações. 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]
plt.plot(x, y)
plt.bar(x, y)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()

# Gráfico de vendas
mouths = ['January', 'February', 'March', 'April', 'May']
sales = [120, 90, 150, 80, 200]
plt.bar(mouths, sales, color='royalblue')
plt.xlabel('Mês')
plt.ylabel('Vendas (unidades)')
plt.title("Vendas Mensais")
plt.show()





# Módulos próprios: desenvolvidos pelo desenvolvedor
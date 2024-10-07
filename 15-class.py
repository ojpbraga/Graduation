# Análise de Dados com Python
# As principais competências é a conexao com banco de dados e bibliotecas em Python.

# Pandas é a mais usada em manipulação de dados e pode gerar gráficos
# É importante saber com dados conflitantes, falta de um dados, uma string no lugar de um int

# Step by Step
# Ter conhecimento a cada dia

# Exercise: suponha que estamos desenvolvendo um programa que gerencia informações de funcionários em uma tabela de um banco de ddos SQLite
import sqlite3

# Conectar banco de dados
conn = sqlite3.connect('funcionarios.db')

# Criar tabela funcionarios
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        cargo TEXT,
        salario REAL
    )
''')

# Inserir um novo funcionario
novo_funcionario = (1, 'João', 'Analista', 5000.0)
cursor.execute("INSERT INTO funcionarios VALUES (?, ?, ?, ?)", novo_funcionario)
conn.commit()

# Consultar e exibir funcionarios
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()
print("Funcionários Cadastrados")
for funcionario in funcionarios:
    print(funcionario)

# Atualiar informações de um funcionário
atualizacao = ("Joao Silva", 5500.00, 1)
cursor.execute("UPDATE funcionarios SET nome = ?, salario = ? WHERE id = ?", atualizacao)
conn.commit()
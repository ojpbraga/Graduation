# Banco de Dados em Python: SQL
# O SQL oferece funcionalidades como junções, subconsultas e transações, que permitem consultas complexas e a manipulação de dados.

# SGBD: Sistema Gerenciador de Banco de Dados
# ODBC e JDBC são interfaces para visualização do banco e ajuda em não recompilar código.

# SQLite
# Biblioteca de banco de dados SQL completa. Funciona sem a necessidade de um servidor separado. Para desenvolvedores Python, oferece um módulo chamado "sqlite3" que permite a interação com SQL.

import sqlite3
# Conectar ao banco de dados (ou criar um novo)
# Se o banco não existir, será criado automaticamente.
connect = sqlite3.connect('exemple.com')

# Criando projeto chamado cursor
# O cursor é usado para executar comandos SQL no banco de dados. É uma espécie de ponteiro que percorre os resultados de consulta.
cursor = connect.cursor()

# Comando para criar tabela
# Definir uma variável create_table que contém um comando SQL para criar uma tabela. Terá quatro colunas: id (chave primária), nome (string), preco (número real) e estoque (int), IF NOT EXISTS garante que só será criada se não existir

create_table = """
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER
);
"""

# Comando para criar a tabela
cursor.execute(create_table)

# Confirmar alterações (commit)
connect.commit()

# Fechar conexão
# connect.close()

# CRUD: Create, Read, Update, Delete
# É uma abordagem fundamental para operações de banco de dados.
# Passos necessários: conexão, criar um cursor, gravar operação, fechar o cursor e conexão.
cursor = connect.cursor()

new_product = ('Shirt', 99.99, 30)

# Comando para inserir o novo produto na tabela:
insert_product = "INSERT INTO Products (name, price, stock) VALUES (?, ?, ?)"

# Executar comando para inserção
cursor.execute(insert_product, new_product)
connect.commit()


# Visualizar
# * Mostra tudo o que tem na tabela
select_product = "SELECT * FROM Products"

cursor.execute(select_product)
produts = cursor.fetchall()
for product in produts:
    print(product)


# Atualizar Produto
# connect = sqlite3.connect('exemple.com')
cursor = connect.cursor()

# Novo price e id do product that will be update
new_price = 12.99
product_id = 3

# Command to updade price
update_price = "UPDATE Products SET price = ? WHERE id = ?"
cursor.execute(update_price, (new_price, product_id))

print("Updated")
select_product = "SELECT * FROM Products"
cursor.execute(select_product)
produts = cursor.fetchall()
for product in produts:
    print(product)

# Exercise

create_table = """
CREATE TABLE IF NOT EXIST Contacts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    cellphone INTEGER NOT NULL,
);
"""

class Contact:
    def __init__(self, name, email, cellphone):
        self.name = name
        self.email = email
        self.cellphone = cellphone
    # I could code others methods here, like update, remove


def add_contact(name, email, cellphone):
    contact = Contact(name, email, cellphone)
    cursor.execute(f"INSERT INTO Contacts (name, price, stock) VALUES ({contact["name"]}, {contact["email"]}, {contact["cellphone"]})")
    connect.commit()
    print(f"Contact {contact.name} is saved!")

def show_contacts():
    cursor.execute("SELECT * FROM Contacts")
    contacts = cursor.fetchall()
    for contact in contacts:
        print(contact)

add_contact("João", "joao@joao.com", 3444444)
add_contact("Ana", "ana@gmail.com", 3466664)
show_contacts()


connect.close()

import matplotlib as plt

class Book:
    def __init__(self, title, author, published):
        self.title = title
        self.author = author
        self.published = published
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.published}"
    
library = []
years_of_publications = []

def add_book(title, author, published):
    new_book = Book(title, author, published)
    library.append(new_book)
    years_of_publications.append(published)
    print(f"The book {title} was added in library")

def list_of_books():
    print("Library books")
    for book in library:
        print(book)

add_book("João e Maria", "KPO", "1002")
add_book("João e M", "LPO", "1002")
add_book("João e Carla", "AW", "1002")
add_book("João e Gislene", "MC", "1002")
add_book("João e Gutto", "SD", "1002")

list_of_books()

# Gráfico
years_of_publications = list(set(years_of_publications))
years_of_publications.sort()

count_books_years = [years_of_publications.count(year) for year in years_of_publications]

plt.plot(years_of_publications, count_books_years, marker='o', linestyle='-')
plt.xlabel("Ano de Publicação")
plt.ylabel("Número de Livros")
plt.title("Distribuição de Livros na Biblioteca por Ano de Publicação")

for i, value in enumerate(count_books_years):
    plt.text(years_of_publications[i], value, str(value), ha="center", va="bottom")

plt.grid(True)
plt.show()
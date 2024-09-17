# Estruturas de repetição
# for: para simplificar tarefas repetitivas, percorrer uma sequência de elementos e executa ações para cada item.
# while
# range, break e continue

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# While
# Repete algo até que a condição seja atendida

number = int(input("Digite um número ou 0 para sair: "))
while number != 0:
    if number % 2 == 0:
        print("O número é par!")
    else:
        print("O número é ímpar!")
    number = int(input("Digite um número ou 0 para sair: "))

# Controle de repetição
# Range
# Repetição por quantidade
print("Quantidade")
for x in range(5):
    print(x)

# Limites Inicial e Superior
print("Inicial e Superior")
for y in range(2, 7):
    print(y)

# Com Incremento
print("Incremento")
for z in range(1, 11, 2):
    print(z)

# Break e continue
for num in range(1, 11):
    if num % 2 == 0:
        print("O primeiro número par encontrado é: ", num)
        break

# Continue - vai pular o número
print("continue")
for num in range (1, 11):
    if num == 5:
        continue
    print(num)

# Aplicando a aula
movies = []
note = int(input("Qual sua nota para o filme 0 (0 para sair)? "))
for num in range(1, 5):
    while note != 0 or num >= 5:
        note = int(input(f'Qual sua nota para o filme {num} (0 para sair)? '))
        movies.append(
        {f'movie{num}': num,
        "note": note
        })
        break
print(movies)
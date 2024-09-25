# Functions
# Built-in: já prontas. Ex:
# print(), int() e range()
# len() valor do tamanho de um array
numbers = [1, 2, 3, 5, 6, "João", True]
print(len(numbers))

# Definidas por usuário: criada pelo usuário
def plus_plus(num):
    num = (num * num)/2
    return num

print(plus_plus(10))

def is_par(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_par(5))

# Anônimas: lambda, função que é utilizada uma vez
is_par_lambda = lambda num: num % 2 == 0
result = is_par_lambda(2)
print(result)

# Exercício
grades = [7.5, 6, 2, 10, 5.8]

def calculate_grade(grades):
    all = sum(grades)
    half_grades = all/len(grades)
    return half_grades

round_grade = lambda half: round(half, 2)

media = calculate_grade(grades)
media_arredondada = round_grade(media)

status = "Approved" if media_arredondada >= 7 else "Disapprove"
print("Notas: ", grades)
print("Média: ", media)
print("Situação: ", status)
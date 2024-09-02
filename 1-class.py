print("Hello World")

# Fluxo de algoritmo
# É a entrada, processamento e sáida.
# É necessário armazenar valores de entrada, e assim surge o conceito de variável, que é nada mais que um espaço na memória RAM.
# O intretador Python consegue estabeleer o tipo de dado da variável.
# Case sensitive

x = 10
name = 'Jonh'
school_grade = 8.75
registration = True

print(type(x))
print(type(name))
print(type(school_grade))
print(type(registration))

# Input
# Campo para entrada de dados
name_input = input("What is your name? ")
print(f'Hello {name_input}!')

# Exemple
grade_1 = int(input("What is your first grade? "))
grade_2 = int(input("What is your second grade? "))
grade_3 = int(input("What is your third grade? "))
grade_4 = int(input("What is your fourth grade? "))

grade_final = (grade_1 + grade_2 + grade_3 + grade_4)/4

if grade_final >= 6:
    print(f'Congradulations your finally grade is {grade_final}!')
    status = "Approved"
else:
    print(f'You can try again! Your grade is {grade_final}!')
    status = "Disapprove"
print(f'Status: {status}')
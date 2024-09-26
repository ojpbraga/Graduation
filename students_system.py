print("*"*20)
print(" "*2+"Sistema de Alunos")
print("*"*20)
print("")

# Variáveis globais
grades = []
count = 0

# Inputs
print(" Primeiro vamos cadastrar suas notas!")
name = input(" Qual seu nome? ")
print("")
grade = str(input(f" Qual a sua nota 1? (CALCULA para calcular notas) ")).upper()

# Função que retorna o status do aluno
def grades_status(result):
    # Caso maior que 7, passou. Menor que 7, demonstrativo da pontuação necessária para passar
    if(result >= 7):
        print(f" Parabéns, {name}! Sua média é {result:.2f}")
    else:
        print(f" {name}, seu esforço foi válido! Foque um pouco mais, falta apenas {7-result:.2f} pontos para aprovação!")
    print("*"*20)
    print(grades)

# Função que realiza a média
def grades_calculate(grades_array):
    # Result é a soma dos números na array dividos pelo tamanho da array
    result = sum(grades_array) / len(grades_array)
    grades_status(result)
    return result

# Função que registra as notas
def grades_register(grade):
    # Verifica se grade é diferente de calcular, caso seja será verificado para entrar na array
    while grade != "CALCULAR":
        # Verificação se é letra ou número
        if not grade.isalpha():
            grade = int(grade)
            grades.append(grade)
            grade = str(input(f" Qual a sua nota {count}? (CALCULAR para calcular notas) ")).upper()
        else: 
            print(" Erro: não aceita letras!")
            grade = str(input(f" Qual a sua nota {count}? (CALCULAR para calcular notas) ")).upper()
    # Caso o input seja "calcular", chamada da função de calcular as notas contidas na array
    else:
        print("")
        print(" Calculando"+5*"*")
        print("")
        grades_calculate(grades)

grades_register(grade)
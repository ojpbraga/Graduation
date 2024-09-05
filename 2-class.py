# Estruturas condicionais
# O objetivo é a tomada de decisão

# Operadores relacionais
# <
# <=
# >
# >=
# ==
# !=
# is
# is not

# Operadores Boolean
# and
# or
# not

# Estruturas Condicionais
# if
# else
# elif

print(1 > 2)
print(3 > 2)
print(1 == 1)

a = 'student'
b = 'teacher'
print(a is b)
print(a is not b)
print(a != b)

age = 25

if age < 18:
    print('You are under age!')
elif (age > 18 and age < 65):
    print('You are adult!')
else:
    print('You are too much old!')

# Cinema
print("="*20)
print(" "*5 + "BILHETERIA")
print("="*20)
print("")
nome = input(" Qual seu nome? ")
idade = int(input(" Qual a sua idade? "))

def filmesDisponiveis(idade, nome):
    if idade < 12:
        print(f' {nome}, o filme disponível para sua idade é FILME 1!')
    elif idade >= 12 and idade < 18:
        print(f' {nome}, o filme disponível para sua idade é FILME 2!')
    else:
        print(f' {nome}, o filme disponível para sua idade é FILME 3!')

filmesDisponiveis(idade, nome)
print("")
print("="*20)
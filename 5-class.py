print("*"*20)
print(" "*4+"Calculadora")
print("*"*20)
print("")

def calculate_discount(value, discount):
    result = value * (discount / 100)
    return result

value = int(input("Qual valor do produto? "))
discount = 0

while discount < 10 or discount > 70:
    discount = int(input("Qual o valor do desconto? "))
    if discount <= 70 and discount >= 10:
        print("Encerrado")
        print(calculate_discount(value, discount))
        break
    else:
        print("DESCONTO ULTRAPASSANDO! Valores entre 10% e 70%")        


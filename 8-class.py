# Classes e Métodos

# Orientação a objetos
# Uma linguagem é considerada orientada a objetos quando incorpora os princípios de abstração e suporta o uso de encapsulamento, herança e polimorfismo.

# Classe vs Objetos
# A classe será um formato que um objeto deve seguir, como ter nome, idade, altura, métodos (ações). Objeto advém de uma classe com os dados declarados, por exemplo, João, 18, 1.8, cumprimentar(), sair()


# Classes em Python
# Atributos: dados que representam o estado do objeto (nome, idade)
# Métodos: definem o comportamento do objeto
# Encapsulamento: combina atributos e métodos de uma entidade, permitindo controlar o acesso a atributos por meio de métodos
# Herança: permite que uma classe herde atributos e métodos de outra
# Polimorfismo: refere-se a várias classes responderem de forma diferente a mesma mensagem

class Person:
    # __init__ é um método construtor, utiliza-se quando a classe é criada
    def __init__(self, name, age, gender):
        # self refere-se a própria classe.
        # Parâmetros são usados para inicializar os atributos da instância.
        self.name = name # Atribui valor de name ao atributo da instância
        self.age = age
        self.gender = gender
    def greet(self):
        return f"Hi! My name is {self.name}"
    def birthday(self):
        self.age += 1

person1 = Person("John", 19, "male")
print(person1.greet())
person1.birthday()
person1.birthday()
print(person1.age)


# Herança
# Reaproveitar classes
class Animal:
    def __init__(self, name):
        self.name = name
    def make_noise(self):
        pass

class Dog(Animal):
    def make_noise(self):
        return "Bark"
    
class Cat(Animal):
    def make_noise(self):
        return "Meow"
        
cat1 = Cat("Girla")
dog1 = Dog("Spike")
print(cat1.name)
print(cat1.make_noise())
print(dog1.make_noise())


# Exercício

class Vehicle:
    def __init__(self, wheels, plate, doors):
        self.wheels = wheels
        self.plate = plate
        self.doors = doors
    def honk(self):
        pass

class Car(Vehicle):
    def __init__(self, wheels, plate, doors):
        super().__init__(4, plate, 4)
    def honk(self):
        return f"The car honked!"
    
class Bicycle(Vehicle):
    def __init__(self, wheels, plate, doors, type):
        super().__init__(2, plate, 0)
        self.type = type

    def honk(self):
        return f"The bicycle honked!"
    
car1 = Car(10, "RG10", 7)
print(car1.doors)

bike1 = Bicycle(1, "JY40R", 7, "BMU")
print(bike1.wheels)
print(bike1.type)




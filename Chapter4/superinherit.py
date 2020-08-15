import random

class Animal(object):
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        print('{} is eating {}'.format(self.name, food))

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shiny', 'Dark', 'Blond'])

    def fetch(self, thing):
        print('{} goes after the {}'.format(self.name, thing))
    

dog1 = Dog('Yumos')
print(dog1.name)
print(dog1.breed)
class Animal(object):
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        print('{} is eating {}'.format(self.name, food))

class Dog(Animal):
    def fetch(self, thing):
        print('{} goes after the {}'.format(self.name, thing))
    
class Cat(Animal):
    def swatstring(self):
        print('{} shreds the string!'.format(self.name))


r = Dog('Rover') # creating a dog object
f = Cat('Casper') # creating a cat object

r.eat('dog food')
r.eat('cat food')
# >>> r.swatstring() # attribute error: dog instance doesnt have this
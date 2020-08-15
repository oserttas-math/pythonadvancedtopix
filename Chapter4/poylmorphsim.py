class Animal(object):
    def __init__(self, name):
        self.name = name 
    
    def eat(self, food):
        print('{} eats {}'.format(self.name, food))

class Dog(Animal):

    def fetch(self, thing):
        print('{} goes after the {}'.format(self.name, thing))

    def show_affection(self):
        print('{} wags tail'.format(self.name))


class Cat(Animal):

    def swatstring(self):
        print('{} shreds the string'.format(self.name) )

    def show_affection(self):
        print('{} purrs '.format(self.name))



for a in (Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Dawg')):
    a.show_affection()


                

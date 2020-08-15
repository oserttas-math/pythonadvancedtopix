import random

class MyClass(object):
    def dothis(self):
        # returns random int including 1 and 10
        self.random_value = random.randint(1,10)



myinstance = MyClass()
# call the class method dothis on the instance
myinstance.dothis()
# call random_value attribute of the self  object in MyClass class
# self is the instance upon which the method was called
print(myinstance.random_value)
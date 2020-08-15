'''You may remember that when I first described classes I called them blueprints for instances a class

defines the attributes that will be set in an instance as well as defining attributes that the instance

can access the class attributes.

So a class really is a kind of a blueprint for an instance.

But when we're working in a collaborative environment with other developers who are creating classes

that will fit into a larger hierarchy we may want to define a class that indicates and enforces what

methods the subclass should implement.

And we call this an abstract class.

'''
import abc

class GetterSetter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod 
    def set_val(self, input):
        '''set a value in the instance'''
        return 

    @abc.abstractmethod 
    def get_val(self):
        '''get and return a value from the instance'''
        return

class MyClass(GetterSetter):
    
    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val

x = MyClass()
print(x)



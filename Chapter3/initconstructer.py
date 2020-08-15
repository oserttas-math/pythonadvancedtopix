''' if we wanted to set some attributes to be set right at the beginning
before an instance is even created.
This can be done in the constructor.'''

class MyNum(object):
    '''Lets create an instance method which will initially
    set an integer value in the instance. creating the val attribute and 
    setting it to 0'''

    def __init__(self):
        print('calling __init__')
        self.val = 0
    '''notice that this function returns nothing,
    so you cannot assign the outcome of this to any variable'''
    def increment(self):
        self.val = self.val + 1





number1 = MyNum()
print(number1)
i = 0
for i in range(3):
    number1.increment()
    i += 1
print(number1.val, 'is', i)
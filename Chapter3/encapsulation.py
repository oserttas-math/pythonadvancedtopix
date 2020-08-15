class MyClass(object):
    # take the val argument and set it as an attribute
    # in the instance under and attrbute called VALUE
    # with a try-except block SETTER function will not let us 
    # assung any value that cannot be converted to an integer 
    # the value attrivute wont be defined due to the value error
    def set_val(self, value):
        try:
            value = int(value)
        except ValueError:
            return 
        self.value = value

    def get_val(self):
        return self.value

    def increment_val(self):
        self.value = self.value + 1




a = MyClass()
b = MyClass()


# a.set_val(10)
# b.set_val(1000)

# # call method
# print(a.get_val())
# # call method
# print(b.get_val())

'''this will throw an error because it is bypassing try except block 
and does not check if the value is an integer'''

# a.value = 'hello man'
# print(a.value)
# print(a.increment_val())

'''BUT if you used set value attribute'''

a.set_val('hi')
print(a.increment_val())
# c = a.increment_val()
# print(c.get_val())
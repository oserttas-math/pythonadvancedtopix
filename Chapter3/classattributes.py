class YourClass(object):
    classy = 'class attribute'

    def set_val(self):
        self.insty = 100 

test = YourClass()
test.set_val()
print(test.insty)
print(test.classy)
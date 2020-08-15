
''' # instance attributes can be the list 
        and the input to instance which is length/size of 
        required list'''

class MaxSizeList(object):
    def __init__(self, length):
        self.size = length
        self.somelist = []

    def push(self, item):
        '''stop accepting new items to list 
        when length is bigger than given size by user'''      
        while len(self.somelist) < self.size:
            self.somelist.append(item)
            break

    def get_list(self):
        return self.somelist



a = MaxSizeList(5)
b = MaxSizeList(4)


print('printing list a \n','-' * 20)
a.push('hi')
a.push('godd')
a.push('bak')
a.push('ali')
a.push('try adding the last sentence')


print(a.get_list()) 
print('printing list b \n','-' * 20)

b.push('cannot beat me')
b.push('try this')
print(b.get_list())


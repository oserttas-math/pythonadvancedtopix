# class InstanceCounter(object):
#     count = 0

#     def __init__(self, val):
#         self.val = val
#         InstanceCounter.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val
#     '''counter is an attribute of the class so we align this method
#     with the its class'''
#     @classmethod
#     def get_count(cls):
#         return cls.count



# a = InstanceCounter(4)
# print(a.get_val())
# print('The nuumber of current instances: {}'.format(a.get_count()))


# b = InstanceCounter(9)
# print(b.get_val())
# print('The nuumber of current instances: {}'.format(b.get_count()))

#######################################################
##########################Static Method################

class NewInstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        NewInstanceCounter.count += 1
    '''utility method which belongs to class and doesnt need a SELF arg'''
    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value


a = NewInstanceCounter(4)
print(a.val)
b = NewInstanceCounter('hello')
print(b.val)

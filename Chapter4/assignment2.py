import abc
from datetime import datetime

'''it’s very helpful to use an abstract class to define a common 
interface for different implementations.'''
class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod 
    def write(self):
        return
    
    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        file_handler = open(self.filename, 'a') # append
        file_handler.write(text + '\n') # with a line changer
        file_handler.close()

class DelimFile(WriteFile):
    
    def __init__(self, filename, delim):
        super(DelimFile, self).__init__

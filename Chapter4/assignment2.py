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
    
    def __init__(self, filename, delim): # delimfile needs a type of delimeter to be specified
        super(DelimFile, self).__init__(filename) # delimfile need a file name so this will do
        self.delim = delim

    '''polymorphisim: here we use the same interface (write method) to do similar things'''
    def write(self, alist):
        line = self.delim.join(alist)
        self.write_line(line)

class LogFile(WriteFile):

    def write(self, aline):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line('{}  {}'.format(date_str, aline))


        



# test it now
log = LogFile(filename='firstlog.txt')
csv_file = DelimFile(filename='firstdata.csv', delim=',')

# polymorphism in acton!
text1 = 'Ah it seems to be working!'
text2 = 'This is just a test!'
log.write(text1)
log.write(text2)


header = ['header1', 'heade2', 'header3', 'header4']
csv_file.write(header)

text3 = 'header is written'
log.write(text3)

first_row = ['entry1', 'entry2', 'entry3', 'entry4']
csv_file.write(first_row)

text4 = 'first row of the file is written'
log.write(text4)
text5 = 'work is complete'
log.write(text5)




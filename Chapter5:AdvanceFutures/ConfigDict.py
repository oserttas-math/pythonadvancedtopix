import os

class ConfigDict(dict):
    # fisrt we create a file in the constructor
    def __init__(self, filename):
        self._filename = filename
        # _ is to indicate this is a private var
        if os.path.isfile(self._filename): # is it a file on the path
            with open(self._filename, 'r') as fh: # if exist open 
                print('creating the txt file')
                for line in fh:
                    line = line.rstrip() # line in file new line added
                    key, value = line.split('=', 1) # max split amount, 1 here on the equal sign
                    dict.__setitem__(self,key, value) # setting value to key with superclass

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fh: # here we open the file we created 
            for key,  val in self.items():
                print('writing the data')
                fh.write('{}={}\n'.format(key, value))
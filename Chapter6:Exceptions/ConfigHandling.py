# If file name does not exist?
# If a path is not valid
# If a key is not valid
# 

import os
class ConfigKeyError(Exception):
    
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()
        
    def __str__(self):
        return 'key "{}" not found. Availabe keys: ({})'.format(self.key, ', '.join(self.keys))
    

class ConfigDict(dict):
    # fisrt we create a file in the constructor
    def __init__(self, filename):
        self._filename = filename
        # _ is to indicate this is a private var
        if not os.path.isfile(self._filename): # is it a file on the path
            try:
                open(self._filename, 'w').close()
            except IOError:
                raise IOError('arg to ConfigDict must be a valid pathname')
        with open(self._filename, 'r') as fh: # if exist open 
            print('opening the txt file')
            for line in fh:
                line = line.rstrip() # line in file new line added
                key, value = line.split('=', 1) # max split amount, 1 here on the equal sign
                dict.__setitem__(self,key, value) # setting value to key with superclass

    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)
    
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'a') as fh: # here we open the file we created 
            #for key,  val in self.items(): # having loop would update all the previous keys with last given value
            print('writing the data')
            fh.write('{}={}\n'.format(key, value))


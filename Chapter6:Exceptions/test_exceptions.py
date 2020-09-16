'''
    Usages:
    ./test.py                                 (reads out the entire config dict)
    ./test.py thatkey                         (prints the value associated with this key)
    ./test.py thiskey thisvalue               (sets 'thiskey' and 'thisvalue' in the dict)
    
    
'''


import sys
import os
from ConfigHandling import ConfigDict

config_file = 'configuration.txt'

if not os.path.isfile(config_file):
    print('Enter a valid path or a file name:')
    x = input()
    cd = ConfigDict(x)
else:
    cd = ConfigDict(config_file)
    
# if 2 arguments on the command line, set a key and value in the object's dictionary
if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('test passed writing data now: "{}", "{}"'.format(key, value))
    cd[key] = value
    
    
# if 1 argument on the command line, treat it as a key and show the value
elif len(sys.argv) == 2:
    print('reading a value')
    key = sys.argv[1]
    print('test passed reading the value for "{}" is "{}"'.format(sys.argv[1], cd[key]))
    
# if no arguments on the command line, show all keys and values
else:
    print('keys/valeus:')
    for key in cd.keys():
        print('test passed reading the entire file "{}" = "{}"'.format(key, cd[key]))
        
        
        
        
        
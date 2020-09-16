# test for asssignment 3
import sys
from ConfigDict import ConfigDict

newdict = ConfigDict('./commandline_config.txt')


if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('writing data: {}, {}'.format(key, value))
    
    newdict[key] = value

else:
    print('reading data')
    for key in newdict.keys():
        print('  {} = {}'.format(key, newdict[key]))
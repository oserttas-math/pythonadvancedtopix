import sys

def doubleit(x):
    var = x * 2
    return var


if __name__ == '__main__':
    input_val = sys.argv[1]
    doubled = doubleit(input_val)
    
    print('the value of {} is {}'.format(input_val, doubled))
    
import math

def negate(value):
    if(value[0] == '-'):
        return value[1:]
    else:
        return '-' + value
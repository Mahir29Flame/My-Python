from functools import reduce
List = [43,678,99838,56,783,838,3838,667,3839,989]
def max(x,y):
    if x>y:
        return x
    return y
print(reduce(max, List))
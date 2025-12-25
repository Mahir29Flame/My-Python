## Mapping example
List = [1,2,3,4,5,6,7,8,9,10]
print(List)

sqr = lambda x: x * x

sqrlist = map(sqr, List)
print(list(sqrlist))
# Converting strings to integers
str_nums = ["1", "2", "3"]
ints = list(map(int, str_nums))
print(ints)

# Mapping with multiple iterables
l1 = [1, 2, 3]
l2 = [10, 20, 30]
added = list(map(lambda x, y: x + y, l1, l2))
print(added)

# Mapping over a tuple
tup = (1, 2, 3)
sqr = lambda x: x * x
tup = map(sqr, tup)
print(list(tup))

## Filtering example

def even(num):
    if num % 2 == 0:
        return True
    return False

List = [1,2,3,4,5,6,7,8,9,10]
even_list = filter(even, List)
print(list(even_list))

## Reducing example
from functools import reduce

def sum(x, y):
    return x + y
print(reduce(sum, List))   # this is basically an example of sequential computation

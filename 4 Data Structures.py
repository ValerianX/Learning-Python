# array - same data types and mutable(values can be changed, sliced, indexed)()
# List - different data types and mutable []
# Tuples - Different datat types but immutable ()
# Set - A set is an unordered collection with no duplicate elements represented by {} similar to dictionary. To create an empty set we use set() and not {} as former creates set and latter creates dict.
# Dictionary - Different data types and mutable but stored in key value pairs {}
# Stacks - append and pop - LIFO
# Collections - append and popleft - FIFO

# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].
#
# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
#
# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
#
# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
#
# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
#
# list.clear()
# Remove all items from the list. Equivalent to del a[:].
#
# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
#
# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
#
# list.count(x)
# Return the number of times x appears in the list.
#
# list.sort(*, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
#
# list.reverse()
# Reverse the elements of the list in place.

# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].

####################################
# List Comprehensions - A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses

a = ['a', 'b', 'c', 'd']
for user in a:  # can not use range(a) here as list can not be interpreted as integer
    print(user)
for alphabet in range(len(a)):
    print(alphabet, a[alphabet])
print(dict(enumerate(a)))
print(tuple(enumerate(a)))
print(list(enumerate(a)))

#######################################################

squares = []
for x in range(1,10):
    squares.append(x**2)
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

#

pair = [(x, y) for x in [1,2,3] for y in [3,1,4] if x!=y]   # try writing this program using lambda function
print(pair)

pair = []
for x in [1,2,3]:
    for y in [3, 1, 4]:
        if x!=y:
            pair.append((x,y))
print(pair)

#

vec = [-4, -2, 0, 2, 4]
vec = list(map(lambda x: x**2, vec))
print(vec)
vec = [-4, -2, 0, 2, 4]
vec = list(map(lambda x:abs(x), vec))
print(vec)
vec = list(map(lambda x:x**3 if x>=0 else x, vec))
print(vec)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([x.rstrip() for x in freshfruit])
# flatten a list using 2 for
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([x for y in vec for x in y])

a = set('hello world')
b = set('shazam')

print(a)        # unique letters in a
print(b)
print(a - b)    # letters in a but not in b
print(a | b)    # letters in a or b or both
print(a & b)    # letters in both a and b
print(a ^ b)    # letters in a or b but not both
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# Dictionaries

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

# Lambda functions, Map, filter, reduce
# Map and Filter are inbuilt functions, for reduce we need to import library

from functools import reduce
q = reduce(lambda x, y: x+y, range(2, 5))
print(q)

# Find largest number in list
list_of_nums = [22,45,32,20,87,94,30]
print(reduce(lambda x,y: x if x>y else y,list_of_nums))

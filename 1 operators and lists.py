a: int = 2
b = a
print(a // b)  # absolute dividend
print(a % b)  # remainder
print(a ** b)  # power

print('doesn\'t')  # "\" is iused as an escape operator
print("doesn't")  # alternatively
print("First Line.\nSecond line")  # \n means new line

print(r'C:\some\name')  # note the r before the quote since \n can be interpreted as next line

# strings can be concatenated using + and repeated using * operator

print('Hello'' ''World')  # String literals are automatically concatenated if + sign is not used between strings
# """...""" Triple quotes are used to concatenate multiple line strings

word = 'Python'
print(word[1:-1])  # array range also called splitting

print(word[:2] + word[-4:-2] + word[4:])
print(len(word))

# LISTS

# In case of an LIST using splitting is also termed as slicing. for ex:

squares = [1, 4, 9, 16, 25]
print(squares[2:-1])  # slicing creates a new list

print(squares + [36, 49])

# Strings are immutable but lists are not as the content can be changed
squares.append(65)
squares[5] = 64
print(squares)

squares[5:] = [0]
print(squares)

squares[5:] = []
print(squares)

squares[2:4] = ['a', 'b']
print(squares)

squares[:] = []
print(squares)

a = [1, 2, 3]
b = ['a', 'b', 'c']
x = [a, b]
print(x)
print(x[1][0])
print('\n')

# Fibonacci series
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b



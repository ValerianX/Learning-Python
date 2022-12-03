import random

x = int(input("Enter an integer : "))
if x<0:
    print("Negative integer")
elif x == 0:
    print("Zero")
elif x == 1:
    print("One")
else:
    print("Big Integer")

#######################################

words = ["apple", "cat", "dog"]
for w in words:
    print(w, len(words))

####################################### list [], collectyions {}, tuples () - can contain listy and also can be converted to listsa and then reconverted back to tuples
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# 1: Iterate over a copy
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]
print(users)

# 2: New collection
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status
print(active_users)

############################################
str_demo = "     hello     _world"
print(str_demo.lstrip())
print(str_demo.split('_'))
one = str_demo.split()
first = one[0]
print(one[1])
print(one, first, '\n', one[1]) # investigate error
print(one, first, '\n', one[1]) # investigate error

###########################################
# Range()

print(sum(range(1, 5)))  # sum 1 to 4 as range starts from 1 and ends on 4

for i in range(1, 10):
    print(i)

list(range(1, 10, 3))

a = ['a', 'b', 'c', 'd']
for i in range(len(a)):  # can not use range(a) here as list can not be interpreted as integer-range takes integers only
    print(i, a[i])

################################
# Fibonacci series

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(5000)







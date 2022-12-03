import numpy as np

# Convert lists or tuples to arrays using np.array()
# np.ones(): Create array of 1s
print(np.ones((5, 3)))                         # axis 0 = 5 and axis 1 = 3

# np.zeros(): Create array of 0s
print(np.zeros((4, 2), dtype=int))

# np.random.random(): Create array of random numbers
print(np.random.randint(1, 9, [4, 5], dtype=np.int64))

# np.arange(): Create array with increments of a fixed step size similar to range
print(np.arange(10, 100, 5))       # From 10 to 100 with a step of 5
print(np.arange(36).reshape(3, 3, 4))       # Tip: 3x3x4 = 36

# np.linspace(): Create array of fixed length
print(np.linspace(15, 18, 25))     # Array of length 25 between 15 and 18

# np.full(): Create a constant array of any number ‘n’
print(np.full((4, 3), 7))

# np.tile(): Create a new array by repeating an existing array for a particular number of times
print(np.tile([0, 1, 2], 3))

# np.eye(): Create an identity matrix of any dimension
print(np.eye(3, dtype=int))

# np.randint(): Create a random array of integers within a particular range
print(np.random.randint(1, 9, (5, 2)))

# create an array
array_1d = np.array([x for x in range(10)])
print(array_1d)

array_2d = np.array([(x, y) for x in range(1, 3) for y in range(2, 4) if x != y])
print(array_2d)

# Arithmetic operations can be performed on lists easily using Numpy instead of complex conventional ways For instance:

list_1 = [3, 6, 7, 5]
list_2 = [4, 5, 1, 7]
product_list = list(map(lambda x, y: x*y, list_1, list_2))      # Conventional lambda or function way
print(product_list)

array_1 = np.array(list_1)
array_2 = np.array(list_2)
array_3 = array_1*array_2           # Array multiplication
print(array_3)
print(list(array_3))                # convert to list
print((array_3*2).tolist())         # convert to list
print(type(array_3))

###########################################
# Indexing and Slicing
# help(np.linspace(1, 3))           help can be used when more syntax and other information is required

a = np.random.randint(1, 10, 10)
print(a)
print(a[[2, 5, 6]])                        # double square bracket for position/index

a = np.array([[3, 7, 7, 4], [6, 3, 2, 8], [2, 6, 2, 3]])
print(a[1:, :2])                           # a[axis 0, axis 1] where axis 0 is rows and axis 1 is columns
a = np.array([[3, 7, 7, 4, 3, 4], [6, 3, 2, 8, 2, 6], [2, 6, 9, 3, 7, 8]])
b = a
print(a[1:, ::2])                          # :: double colon represents a fixed increment. Here after every 2 index

print("Shape: {}".format(a.shape))
print("dtype: {}".format(a.dtype))
print("Dimensions: {}".format(a.ndim))
print("Item size: {}".format(a.itemsize))
print("Shape: ", a.shape)
a = a.reshape(9, -1)         # -1 means "whatever dimension is needed"
print(a)
print("\n")
print(a.T)                      # Transposing an array
print("\n")
print(b)
print("\n")

###############################
# Stacking arrays - np.vstack(), np.hstack()

array_1 = np.arange(6).reshape(3, 2)            # Dimensions should match y axis or axis 1 here
array_2 = np.arange(10).reshape(5, 2)           # Dimensions should match y axis or axis 1 here
new_array1 = np.vstack((array_1, array_2))      # Array here has to be defined as a list
print(new_array1)

print("\n")

array_1 = np.arange(6).reshape(2, 3)            # Dimensions should match x axis or axis 0 here
array_2 = np.arange(10).reshape(2, 5)           # Dimensions should match x axis or axis 0 here
new_array2 = np.hstack((array_1, array_2))      # Array here has to be defined as a list
print(new_array2)

##################################
# Operations on arrays
a = np.arange(1, 20)
print(np.sin(a))
print("\n")
print(np.cos(a))
print("\n")
print(np.exp(a))
print("\n")
print(np.log(a))
print("\n")

# np.linalg.inv: Inverse of a matrix
# np.linalg.det: Determinant of a matrix
# np.linalg.eig: Eigenvalues and eigenvectors of a matrix

a = np.arange(1, 17).reshape(4, 4)
print(np.linalg.inv(a))
print("\n")
print(np.linalg.det(a))
print("\n")
print(np.linalg.eig(a))
print("\n")
a = np.arange(1, 10).reshape(3, 3)
b= np.arange(1, 13).reshape(3, 4)
print(np.dot(a, b))
print("\n")

# User Defined Functions
f = np.vectorize(lambda x: x/(x+1))         # This function once defined can be used on any array
f(a)




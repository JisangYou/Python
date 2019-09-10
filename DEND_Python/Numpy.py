import time
import numpy as np

x = np.random.random(100000000)

# 14.688855171203613초

# start = time.time()
# sum(x) / len(x)
# print(time.time() - start)

# 0.1410841941833496초 

# start = time.time()
# np.mean(x)
# print(time.time() - start)

x = np.array([1, 2, 3, 4, 5])

print(x)
print(type(x))
print()

# We print x
print()
print('x = ', x)
print()

# We print information about x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# We create a rank 2 ndarray that only contains integers
Y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# We print Y
print()
print('Y = \n', Y)
print()

# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y has a total of', Y.size, 'elements')
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)


# We save x into the current directory as
np.save('my_array', x)
# We load the saved array from our current directory into variable y
y = np.load('my_array.npy')

# We print y
print()
print('y = ', y)
print()

# We print information about the ndarray we loaded
print('y is an object of type:', type(y))
print('The elements in y are of type:', y.dtype)
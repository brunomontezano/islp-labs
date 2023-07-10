# Print some text with print()
print("Fit a model with", 11, "variables.")

# Addind two integers
3 + 5

# Concatenating strings
"Hello" + " " + "world"

# Create a list
x = [3, 4, 5]
x

# Create another list
y = [4, 9, 7]

# It's interesting that adding two lists do not behave like in R
# The second list is appended to the first one!
x + y

# Import numpy to work with some numerical Python
import numpy as np

# Transform both lists into numpy arrays
x = np.array ([3, 4, 5])
y = np.array ([4, 9, 7])

# And now when we sum up these values they output something like you would
# expect in R
x + y

# Now let's multiply the vectors
x * y

# Matrices in Python are usually represented as two-dimensional arrays and
# vectors as one-dimensional arrays
x = np.array([[1, 2], [3, 4]])
x

# The object x has several attributes, we can access it like x.attribute
# Let's get the number of dimensions for the x object
x.ndim

# Now let's get the data type
x.dtype

# If we have at least one floating point number, dtype outputs float64
np.array([[1, 2], [3.0, 4]]).dtype

# Or I could build it explicitly
np.array ([[1, 2], [3, 4]], float).dtype

# The shape attribute shows the number of rows and columns of the object
x.shape

# Method is a function that is associated with an object
# sum() can sum all elements of a given array
x = np.array([1, 2, 3, 4])
x.sum()

# Another way would be using the sum() function from numpy library()
x = np.array([1, 2, 3, 4])
np.sum(x)

# reshape() method returns a new array with the same elements, but a different shape
x = np.array ([1, 2, 3, 4, 5, 6])
print('Beginning x:\n', x)
x_reshape = x.reshape ((2, 3))
print('Reshaped x:\n', x_reshape)

# Python uses row-major ordering and 0-based indexing

# Accessing the top left element of x_reshape
x_reshape[0, 0]

# Element in the second row and the third column of x_reshape
x_reshape[1, 2]

# Third entry of x
x[2]

# Modifying the top left element of x_reshape
print('x before we modify x_reshape :\n', x)
print('x_reshape before we modify x_reshape :\n', x_reshape)
x_reshape [0, 0] = 5
print('x_reshape after we modify its top left element :\n', x_reshape)
print('x after we modify top left element of x_reshape :\n', x)

# Modifying x_reshape also modified x because the two objects occupy the same
# space in memory

# Trying to modifying a tuple and failing...
my_tuple = (3, 4, 5)
my_tuple [0] = 2

# Interestingly, the output of the code below is a tuple itself
x_reshape.shape, x_reshape.ndim, x_reshape.T

# What is x?
print(x)

# Calculate square root of x elements
np.sqrt(x)

# We can square the elements
x ** 2

# Square root using the same notation, raising to the power of 1/2 instead of 2
x ** 0.5

# We can also generate random data
# The function np.random.normal() generates a vector of random normal variables
# Arguments are loc, scale and size
# loc is the mean; default 0
# scale is the standard deviation; default 1
# size is the sample size; default 1

# Generate random human heights
x = np.random.normal(loc = 175, scale = 10, size = 50)
print(x)

# Let's make them a little taller
y = x + np.random.normal(loc = 30, scale = 1, size = 50)
print(y)

# We can calculate the correlation matrix between x and y
np.corrcoef(x, y)

# The results are always different because we did not set a seed
print(np.random.normal(scale=5, size =2))
print(np.random.normal(scale=5, size =2))

# We can set a seed, it's not a problem!
rng = np.random.default_rng (1303)
print(rng.normal(scale=5, size =2))
rng2 = np.random.default_rng (1303)
print(rng2.normal(scale=5, size =2))

# np.mean(), np.var(), np.std() can be used to calculated mean, variance and
# standard deviations
rng = np.random.default_rng (3)
y = rng.standard_normal (10)
np.mean(y), y.mean()

np.var(y), y.var(), np.mean((y - y.mean())**2)

# np.var() divides by the sample size n rather than n - 1 by default
# See argument ddof in np.var()
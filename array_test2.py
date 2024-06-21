# Task

# You are given a 2-D array of size N x M.
# Your task is to find:
# The mean along axis 1
# The var along axis 0
# The std along axis None

# Input Format
# The first line contains the space separated values of N and M.
# The next N lines contain M space-separated integers.

# Output Format
# First, print the mean.
# Second, print the var.
# Third, print the std.

# Sample Input
# 2 2
# 1 2
# 3 4

# Sample Output
# [ 1.5  3.5]
# [ 1.  1.]
# 1.118033988750

import numpy as np

# Get the dimensions of the array and create an empty array
# n, m = input('Enter rows and columns, separated by spaces: ').strip().split(' ')
n, m = input().strip().split(' ')
n = int(n)
m = int(m)
my_array = np.zeros([n, m])

# Report what we've done so far ...
# print(f'The values entered are: n = {n} and m = {m}.')
# print(f'Created empty array of dimension {n} x {m}')
# print(my_array)

# Get the data to put in the array elements
for row in range(n):
    my_array[row] = [int(x) for x in input().strip().split(' ')]

# Report the contents of the populated array
# print('Populated array:')
# print(my_array)

# Print the required statistics, as per the assignment question:
print(np.mean(my_array, axis = 1))      # Mean along axis 1 - the rows
print(np.var(my_array, axis = 0))       # Variance along axis 0 - the columns
print(round(np.std(my_array, axis = None), 11))    # Standard deviation for axis None, i.e. the whole array

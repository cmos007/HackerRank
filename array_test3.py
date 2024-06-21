"""
TASK:
You are given two arrays A and B, each of dimension N x N
The requirement is to compute their matrix product
The dimensions and array contents must be read from standard input
The matrix product must be written to standard output

INPUT FORMAT
The first line contains the array dimension: N
The next N lines contain the rows of array A
The following N lines contain the rows of array B

OUTPUT
Print the matrix product of A and B

SAMPLE INPUT:
2
1 2
3 4
1 2 
3 4

SAMPLE OUTPUT
[[7 10]
[15 22]]
"""

import numpy as np

# Read the array dimension
n = int(input().strip())
a = np.zeros([n, n], dtype = int)
b = np.zeros([n, n], dtype = int)

# Read the first array
for row in range(n):
    a[row] = [int(x) for x in input().strip().split(' ')]

# Read the second array
for row in range(n):
    b[row] = [int(x) for x in input().strip().split(' ')]

# Calculate the matrix product
# The dimension will also be nxn, as the arrays are square
c = np.zeros([n, n], dtype = int)
for row in range(n):
    for col in range(n):
        for k in range(n):
            c[row,col] += a[row, k]*b[k, col]

# Output the result
print(c)

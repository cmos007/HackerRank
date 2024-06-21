# Problem from HackerRank - input a list of elements from standard input
# and calculate the maximum absolute difference of any 2 of the elements
# of the list
# Example input:
# 3
# 1 2 5
# Calculation should return 4, as three pairs of numbers can be made from this list
# and the absolute differences are:
# | 1 - 2 | = 1
# | 1 - 5 | = 4
# | 2 - 5 | = 3
# Of these, 4 is the biggest

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # We treat the differences between the elements of the list as a matrix of rows and columns 
    # and look only at the numbers in the upper half of the matrix. We ignore the main diagonal, 
    # as those differences are 0 anyway. We don't check the lower half of the matrix either, as 
    # that would simply be duplicating calculations already done (because the check is for the 
    # absolute value of the difference of eqch pair of elements, and not the pure difference).
    # If the length of the list is n, the number of calculations/comparisons to be done is
    # S(n-1) where S(n) = the sum of the first n natural numbers.
    # S(n-1) = n(n-1)/2
    
    # def computeDifference(self):
    #     for row in range(len(self.__elements)-1):
    #         for col in range(row + 1, len(self.__elements)):
    #             diff = abs(self.__elements[row] - self.__elements[col])
    #             if diff > self.maximumDifference:
    #                 self.maximumDifference = diff
        
    def computeDifference(self):
        self._sorted = self.__elements[:]   # Make a shallow copy
        self._sorted.sort()                 # Sort it
        self.maximumDifference = abs(self._sorted[0] - self._sorted[-1])

    # Another way to solve this problem would be to sort the list and take the
    # maximum absolute difference as the absolute value of the first element 
    # minus the last element

# End of Difference class

# _ = input()
# a = [int(e) for e in input().split(' ')]

a = [1, 5, 2]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

import numpy as np

my_array = np.array([ [1, 2], [3, 4] ])

print ('Array used:')
print (my_array)
print ()
print('Array elements:')
for row in range(2):
    for col in range(2):
        print (f'Array[{row},{col}] =', my_array[row,col])
print()
print('Array statistics:')
print ('mean: axis 0 (columns):', np.mean(my_array, axis = 0))        #Output : [ 2.  3.]
print ('mean: axis 1 (rows):', np.mean(my_array, axis = 1))        #Output : [ 1.5  3.5]
print ('mean: axis = None:', np.mean(my_array, axis = None))     #Output : 2.5
print ('mean: no arguments:', np.mean(my_array))                  #Output : 2.5

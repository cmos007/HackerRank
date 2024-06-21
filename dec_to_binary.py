import math
import os
import random
import re
import sys

# Hackerrank - 30 days of Code challenge - day 10
# Find the maximum length of a string of consecutive 1's in the binary 
# conversion of a specified decimal number

if __name__ == '__main__':
    # n = int(input().strip())  # We don't bother to read the number for now
    first = random.randint(1000,1000000)
    last = first + 21
    for n in range(first,last):
        decimal = n
        binary = ''
        while decimal != 0:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2
        ones_found = re.findall('1+', binary)
        lengths = { len(s) for s in ones_found }
        print(f'{n} in base 10 = {binary} in base 2. Longest string of ones has length {max(lengths)}.')

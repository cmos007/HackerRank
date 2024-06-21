# Program to calculate the LCM of an input number
# Formula: LCM(a,b) = (a * b ) / GCD(a,b)
# We find the greatest common divisor using Euclid's algorithm

def gcd(a,b):
    # We assume that a is the larger number
    # If this is not the case, swap them round
    if b>a:
        a,b = b,a
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b

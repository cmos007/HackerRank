import math as m

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    save_n = n
    factors = []

    # Check for even factors
    f = 2
    while n%2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check if we need to consider odd factors
    s = m.sqrt(n)
    f = 3
    # print ('Checking for odd factors ...')
    while n>1 and f <= s:
        # print(f'n = {n}, current factor = {f}, current square root = {s}')
        while n%f == 0:
            factors.append(f)
            n = n // f
            s = m.sqrt(n)
        f += 2

    if n>1:     # Check for final large factor
        factors.append(n)

    print(f'The factors of {save_n} are {factors}.')
    # print(factors[-1])

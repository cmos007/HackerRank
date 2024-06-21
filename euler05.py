# Euler problem #5
# What is the smallest number that is divisible with no remainder by all of the numbers from 1 to N
# 1 <= N <= 40

primes = [2,3,5,7,11,13,17,19,23,29,31,37]      # All of the primes in the range 1 to 40

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    factors = {p:0 for p in primes}
    # print(factors)
    # Now we factorise each number from 1 to N
    # and store the highest power of each factor
    # found in the dictionary
    # This is used to calculate the LCM requested
    for i in range(2,n+1):  # We need to ensure N is included
        current_number = i
        # print(f'Factorising {current_number} ...')      # Debug
        for p in primes:
            factor_count = 0
            while current_number %p == 0 and current_number > 1:
                factor_count += 1
                current_number = current_number // p
            # if factor_count > 0:                                # Debug
            #     print(f'   * Found factor {p}^{factor_count}')  # Debug
            if factor_count > factors[p]:
                factors[p] = factor_count
            if current_number == 1:
                break
    product = 1
    for p in factors:
        product *= pow(p, factors[p])

    print(product)

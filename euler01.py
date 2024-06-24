import sys
import random as r

def sum_to_n(n, difference):
    if n>0:
        return difference * n * (n+1) // 2
    return 0

def calc_slow_sum(n):
    sum = 0
    for i in range(2, n):
        if (i%3 == 0) or (i%5 ==0):
            sum += i
    return sum

# Loop through some values
success_count, fail_count = 0, 0

for loop_counter in range(650, 700):
    # n = r.randint(1,100)
    n = loop_counter

# Calculate the results
    max3 = (n-1) // 3
    max5 = (n-1)  // 5
    max15 = (n-1) // 15
    s3 = sum_to_n(max3, 3)
    s5 = sum_to_n(max5, 5)
    s15 = sum_to_n(max15, 15)
    quick_sum = s3 + s5 - s15
    slow_sum = calc_slow_sum(n)
    if quick_sum == slow_sum:
        outcome = 'Match'  
        success_count += 1
    else:
        outcome = '-'*5
        fail_count += 1

    # print(f's3  = {s3}')
    # print(f's5  = {s5}')
    # print(f's15 = {s15}')

    print(f'n = {n}, quick sum = {int(s3 + s5 - s15)}, slow sum = {slow_sum}, comparison = {outcome}')

# Report summary statistics ...
print(f'Success count: {success_count}')
print(f'Fail count:    {fail_count}')

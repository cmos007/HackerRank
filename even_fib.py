t = int(input('How many even sums do you want to generate? ').strip())
for a0 in range(t):
    n = int(input('Please enter series limit: ').strip())
    fib = [1,1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    if fib[-1] > n:
        del fib[-1]
    even_fib = [f for f in fib if f%2 == 0]
    print('Sequence generated:', fib)
    print('The sum of the even Fibonacci numbers <=', n, 'is', sum(even_fib))

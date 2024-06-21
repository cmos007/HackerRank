t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fib = [1,1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    if fib[-1] > n:
        del fib[-1]
    even_fib = [f for f in fib if f%2 == 0]
    print(sum(even_fib))
    

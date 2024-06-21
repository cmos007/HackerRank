
# Calculate the primes in the range 1-120,000 using a sieve of Eratosthenes
limit = 120000
numbers = {i+1:1 for i in range(limit)}
numbers[1] = 0

# Run the sieve ...

for pos in range(2, limit+1):
    if numbers[pos] == 1:
        for j in range(2*pos, limit+1, pos):
            numbers[j] = 0

primes = [n for n in numbers if numbers[n] == 1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primes[n-1])

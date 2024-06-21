def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    check = n - 1
    palindrome = 0
    while check >= 101101 and palindrome == 0:       # We only keep checking while we haven't found one
        while not is_palindrome(check):
            check -= 1
        if is_palindrome(check):
            # print(f'Found palindrome: {check}')
        # Found a palindrome, now we check if we can find 2 3-digit factors, not necessarily prime
            f = 999
            while f>100 and palindrome == 0:            # We only keep checking while we haven't found one
                # print(f'Checking factor {f} ...')
                if check%f == 0:
                    other_factor = check // f
                    if other_factor >= 100 and other_factor < 1000:
                        palindrome = check
                        # print(f'Found factors {f} and {other_factor}')
                f -= 1
        check -= 1  # If the palindrome we already checked did not work, try find another one
    print (palindrome)

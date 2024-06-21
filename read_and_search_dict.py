# Hackerrank challenge to read a specified number of entries from standard input 
# in the form 'name number' and put them into a dictionary
# An arbitrary number of names is then read from standard input and 
# the dictionary is searched for those names. If a name read from standard
# input is found in the dictionary, its number is printed, otherwise 'Not found' is displayed

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input().strip())    # Get the number of name/number entries to read

numbers = {}                # Initialise dictionary

for i in range(n):          # Read in the dictonary entries
    name, number = input().strip().split(' ')
    numbers.update({name:number})

while True:                 # Read the search strings, however many there are
    try:
        search_string = input().strip()
        if search_string in numbers:
            print(f'{search_string}={numbers[search_string]}')  # and display the names if found
        else:
            print('Not found')      # Otherwise display Not found
    except EOFError:                # If there is no more input, we stop
        break
    
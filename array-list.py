''' 1) given an array with some integer type values. 
write a python script to sort array values ?'''

# Sample array

arr = [34, 12, 5, 67, 23, 89, 1, 90]

# Sorting the array
arr.sort()

# Printing the sorted array
print("Sorted array:", arr)


''' 2) given a list of heterogenous elements. 
write a python script to remove all the non int values from the list'''

# Sample list with heterogeneous elements
lst = [23, 'hello', 3.14, 42, True, 67, 'world', 98, None]

# Create an empty list to store only integer values
int_values = []

# Loop through each element in the list
for item in lst:
    if isinstance(item, int):
        int_values.append(item)

# Print the list with only integer values
print("List with only integer values:",int_values)


'''3) write a python script to calculate average of elements of a list'''

# Sample list of numbers
lst = [10, 20, 30, 40, 50]

# Calculating the average
average = sum(lst) / len(lst)

# Printing the average
print("The average is:", average)


'''4) write a python script to create a list of first N prime numbers '''

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate the first N prime numbers
def generate_primes(n):
    primes = []
    num = 2  # Starting from the first prime number
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Input: Number of prime numbers to generate
N = 10

# Generating the list of first N prime numbers
prime_list = generate_primes(N)

# Printing the list of prime numbers
print("First", N, "prime numbers:", prime_list)


'''5) write a python script to create a list of first n terms of a fibonacci series'''

# Function to generate the first n terms of the Fibonacci series
def fibonacci(n):
    fib_list = []
    
    # Initialize the first two terms
    a, b = 0, 1
    
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
        
    return fib_list

# Input: Number of terms to generate
N = 10

# Generating the list of the first N Fibonacci numbers
fib_series = fibonacci(N)

# Printing the list of Fibonacci numbers
print("First", N, "terms of the Fibonacci series:", fib_series)

# Fibonacci sequence problem : Write a program to get nth number in the Fibonacci series.
# Solution 1: Using Iteration

def iteration_fib(n):

  # Setting up starting point.
  a = 0
  b = 1

  for i in range(n):
    # Use tuple unpacking method of Python
    # This is like a = b and b = a+b . This python style makes sure that variables are assigned in correct order.
    a, b = b, a+b
    # print(a,' ',b)
  return a


print(iteration_fib(10))

# Solution 2: Using Recursion


def recursion_fib(n):

  # Check base case
  if n == 0 or n == 1:
    return n

  # Recursion case
  else:
    return recursion_fib(n-1) + recursion_fib(n-2)


print(recursion_fib(10))

# Solution 3 : Using Memoization / Dynamic Programming

# Setup the cache
n = 10
cache = [None]*(n+1)
# print(cache)


def dynamic_fibonacci(n):
  # Check base case
  if n == 0 or n == 1:
    return n

  # Checking the cache
  if cache[n] != None:
    return cache[n]

  # Set the cache
  cache[n] = dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)

  return cache[n]


print(dynamic_fibonacci(10))

# Provide a fibonacci series function that returns the nth number in the series
# Way 1 : Using Loops
def fib1(n):

  a, b = 1, 1

  for i in range(n-1):
    a = b
    b = a+b
    #print(a)
  return a


print(fib1(5))

# Way2: Using Recursion


def fib2(n):
  if n == 1 or n == 2:
    return 1

  return fib2(n-1)+fib2(n-2)


print(fib2(5))

# Way 3: Using Generators:
# Reference : https://realpython.com/introduction-to-python-generators/
a, b = 0, 1


def fib3():
  global a, b
  while True:
    a = b
    b = a+b
    yield a


f = fib3()
next(f)
next(f)
next(f)
next(f)
next(f)
next(f)

print(next(f))


# Way 4: Using memoization
class Memoize:

  def __init__(self, fn):
    self.fn = fn
    self.memo = {}

  def __call__(self, arg):
    if arg not in self.memo:
      self.memo[arg] = self.fn(arg)
      return self.memo[arg]


# Decorator
@Memoize
def fib4(n):
  a, b = 1, 1
  for i in range(n-1):
    a = b
    b = a+b
  return a


print(fib4(5))


def memoize(fn, arg):
  memo = {}
  if arg not in memo:
    memo[arg] = fn(arg)

  return memo[arg]


print(memoize(fib4, 6))
print(memoize(fib4, 89))
print(memoize(fib4, 56))


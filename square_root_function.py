# Find a square root of a number rounted to the nearest integer
# A square root of a given non negative number is always between 1 & n/2
# Complexity : O(n)

def sqrt(num):

  # Check base case :
  if num < 0:
    return ValueError

  if num == 1:
    return 1

  for k in range(int((num/2)+1)):
    if k**2 == num:
      return k

    elif k**2 > num:
      return k-1

  return k


print(sqrt(17))

# Optimize the function using binary search
# Complexity : Olog(n)


def sqrt_binary_search(num):

  if num < 0:
    raise ValueError

  if num == 1:
    return 1

  low = 0
  high = (num/2)+1

  while low+1 < high:

    # Apply binary search
    mid = low + int((high-low)/2)
    square = mid**2

    if square == num:
      return mid

    elif square < num:
      low = mid

    else:
      high = mid

  return low

print(sqrt_binary_search(17))
print(sqrt_binary_search(9100000000000000000000))
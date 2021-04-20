# Find if the sum of two numbers is equal to a target number.
# Use set data structure.

def two_sum(list, target):
  seen = set()

  for num in list:
    num2 = target - num
    if num2 in seen:
      return True

    seen.add(num)

  return False


print(two_sum([3, 6, 5], 9))

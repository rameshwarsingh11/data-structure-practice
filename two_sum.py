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


# Another efficient solution :
def twoSum(arr, target):
      seen = {}
      for i, v in enumerate(arr):
            remaining = target - v
            print(remaining)
            if remaining in seen:
                print('seen[remaining]', seen[remaining])
                return [seen[remaining], i]
            seen[v] = i
            print('seen', seen)
      return []


target = 6
arr = [1, 2, 3,4]
print(twoSum(arr, target))

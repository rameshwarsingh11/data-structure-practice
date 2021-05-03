# Find the number of ways or pairs of elements in a given array to sums to a given number k

import math


def numberOfWays(arr, k):
	# Write your code here

  # Check base cases :
  if len(arr) < 2:
    return 'Number of ways = ' + str(0)

  if len(arr) < 3 and (arr[0] == arr[1] == k):
    return 'Number of ways = ' + str(2)

  # Sets for tracking
  seen = []
  output = []

  for num in arr:
    print('num', num)
    target = k-num
    print('target', target)

    if target not in seen and target != num:
      seen.append(num)

    else:
      output.append(
          (num if num == target else min(num, target), max(num, target)))

    print('seen', seen)
    print('output', output)
    print('============')
  return 'Number of ways = '+str(len(output))


arr = [1, 5, 3, 3, 3]
# expected : Number of ways 4
# arr =  [1, 2, 3, 4, 3] # Failing for this scenario. Need to fix the issue.
#arr = [6]
# expected : Number of ways 2
# actual output : Number of ways 3
k = 6
print(numberOfWays(arr, k))

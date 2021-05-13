# Find the largest sum of array numbers
# Solution Algorithm : If all the elements in the array are positive, just add all the number and get the total sum as answer.
# For mixed sequence ( positive and negative ), take a variable to hold to maximum sum, update it as you move along till you keep getting sum greater than this sum variable.
# Update the sum variable. Don't set it to 0 because it might happen that all the values provided in the array are negative. When the sum starts getting a negative sign, stop.


def largest_countinous_sum_array(array):

  # Performing edge case check here. If array len is zero, return 0
  if len(array) == 0:
    return 0

  # Setting max sum and current sum is zero
  max_sum = current_sum = array[0]

  for num in array[1:]:
    current_sum = max(current_sum + num, num)
    max_sum = max(current_sum, max_sum)

  return max_sum


def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'

  if expected == output:
    print(rightTick, 'Test passed!')

  else:
    print(wrongTick, 'Test failed.')


if __name__ == '__main__':
  expected = 17
  arr = [1, 2, 3, 4, -1, -2, 0, 10]
  output = largest_countinous_sum_array(arr)
  check(expected, output)
  print(output)

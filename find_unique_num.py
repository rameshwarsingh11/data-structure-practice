# Find the non duplicated digit in a number
# Use Exclusive OR Operation XOR
def non_duplicate_number(number_list):

  unique_id = 0

  for i in number_list:
    unique_id ^= i

  return unique_id


def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if expected == output:
    print(rightTick, 'Test passed!')

  else:
    print(wrongTick, 'Test failed.')


if __name__ == '__main__':
    expected = 50
    arr = [10, 20, 30, 10, 20, 30, 50]
    output = non_duplicate_number(arr)
    check(expected, output)
    print(output)

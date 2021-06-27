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
    expected_1 = 50
    arr_1 = [10, 20, 30, 10, 20, 30, 50]
    arr_2 = [20,20,40,9890,78]
    expected_2 = 9924
    output_2 = non_duplicate_number(arr_2)
    output_1 = non_duplicate_number(arr_1)
    check(expected_1, output_1)
    check(expected_2, output_2)
    print(output_1)
    print(output_2)

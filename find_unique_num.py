# Find the non duplicated digit in a number
# Use Exclusive OR Operation XOR
def non_duplicate_number(number_list):

  unique_id = 0

  for i in number_list:
    unique_id ^= i

  return unique_id


print(non_duplicate_number([10, 20, 30, 10, 20, 30,50]))

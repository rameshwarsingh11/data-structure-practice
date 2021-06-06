# Problem : Check if a string containing multiple parentheses is balanced or not

def balance_check(string):
  # Check the edge case first. If there is even number of brackets in the string, we can continue processing the string. Otherwise send an error response / return False.
  if len(string)%2 !=0:
    return False

  opening_brackets = set('({[')
  matching_set = set([('(',')'),('{','}'),('[',']')])
  stack = []

  for parenthesis in string:
    if parenthesis in opening_brackets: # To make sure we are accepting the correct opening brackets only.
      stack.append(parenthesis)
    
    else:
      if len(stack) == 0:
        return False
    
      last_open = stack.pop()

      if (last_open,parenthesis) not in matching_set:
        return False
  return len(stack) == 0

def check(expected, output):
  rightTick = '\u2713'
  wrongTick = '\u2717'

  if expected == output:
    print(rightTick, 'Test passed.')

  else:
    print(wrongTick, 'Test failed.')

if __name__ == '__main__':
  str_1 = '{}{{}}({)]'
  str_2 = '(((}}}[][]'
  str_3 = '[{()}]'
  output_1 = balance_check(str_1)
  expected_1 =  False
  check(expected_1, output_1)
  output_2 = balance_check(str_2)
  expected_2 = False
  check(expected_2, output_2)
  output_3 = balance_check(str_3)
  expected_3 = True
  check(expected_3, output_3)

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

print(balance_check('{}{{}}({)]'))
print(balance_check('(((}}}[][]'))
print(balance_check('[{()}]'))

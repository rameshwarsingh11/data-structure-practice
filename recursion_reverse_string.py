# Recursion
# Reverse a string using recursion

def reverse_string(string):
  # Check base case
  if len(string) <= 1:
    return string
  
  # Recursive case
  return reverse_string(string[1:]) + string[0]

print(reverse_string('Abracadabra'))
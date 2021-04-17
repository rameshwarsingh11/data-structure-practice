# Recursion function to reverse a string
def reversestring(s):

  # Check base case:
  if len(s) <= 1:
    return s

  # Reverse the given string using recursion:
  return reversestring(s[1:]) + s[0]


print(reversestring('Hello'))

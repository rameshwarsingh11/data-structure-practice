# Rotate a string for encryption
def rotational_cipher(string, r_factor):
  if not string or not r_factor:
    return string
# Built in python function chr() method converts an integer to character and ord() does the opposite.
  cap_alpha = [chr(c) for c in range(ord("A"), ord("Z")+1)]
  print(cap_alpha)
  alpha = [chr(c) for c in range(ord("a"), ord("z")+1)]
  print(alpha)
  res = []

  for c in string:
    if not c.isalnum(): #isalnum() returns true if all the characters in the string are alphanumeric.
      res.append(c)

    elif c.isalpha(): # isalpha() returns true if all the characters in the string is alphabets.
      if c.isupper():
        idx = cap_alpha.index(c) + r_factor
        if idx > 25:
            idx %= 26
        res.append(cap_alpha[idx])
      else:
        idx = alpha.index(c) + r_factor
        if idx > 25:
          idx %= 26

        res.append(alpha[idx])
    elif c.isdigit():
      res.append(str(int(c) + r_factor)[-1])
      print(str(int(c) + r_factor))
  return "".join(c for c in res)


print(rotational_cipher('abcd-90', 2))
print(rotational_cipher('9856-abcb1234ltd-io90', 8))

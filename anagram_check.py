# Anagram example
# Find if two strings having same letter
# Primary solution ( not very optimal)
def anagram(s1, s2):
  #cleanup the strings and lower the characters
  s1 = s1.replace(' ', '').lower()
  s2 = s2.replace(' ', '').lower()

  return sorted(s1) == sorted(s2)

# More optimal solution


def anagram2(s1, s2):
    #cleanup the strings and lower the characters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    #Doing an edge case:
    # If both strings not have the same number of letters then return False

    if len(s1) != len(s2):
      return False

    count = {}  # Dictionary

    for letter in s1:
      if letter in count:
        count[letter] += 1
      else:
        count[letter] = 1

    for letter in s2:
      if letter in count:
        count[letter] -= 1

      else:
        count[letter] = 1

    for k in count:
      if count[k] != 0:
        return False

    return True


#print(anagram('God forbid', 'Bid for dog'))
#print(anagram2('God forbid', 'Bid for dog'))

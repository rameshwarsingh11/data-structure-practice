# Problem : Find out if a string has all unique chracters.
# Solution 1 : Using a built in data structure with function.
def unique_character(string):
  return len(set(string)) == len(string)

print(unique_character('cfghiit'))

# Solution 2 : Create a lookup function
def unique_character2(string):
  characters = set()
  for letter in string:
    if letter in characters:
      return False
    else:
      characters.add(letter)

  return True

print(unique_character2('cfghit'))
print(unique_character('cfghit'))
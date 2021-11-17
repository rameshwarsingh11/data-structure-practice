# Remove duplicates and keep the first occurrences in the list
# Time complexity : O(n) where n is the number of characters.
def remove_duplications(str):
  result = []
  seen = set()

  for char in str:
    if char not in seen:
      seen.add(char)
      result.append(char)
  return ''.join(result)


print(remove_duplications('My Monkey KeyMon Monkey Mon keyMon.'))
#remove_duplications('My Monkey.My Monkey2.My Monkey3.My Donkey.My Monkey.My Monkey.My Honk.My Monkey.My Monkey3.My Monkey3.My Monkey.')
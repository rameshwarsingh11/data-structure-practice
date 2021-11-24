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
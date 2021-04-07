# Sequential Search
# Best case O(1), worst case O(n)
# For unordered list
def seq_search(arr, element):
  pos = 0
  found = False  # This variable will become True when we get the element.
  while pos < len(arr) and not found:

    if arr[pos] == element:
      found = True

    else:
      pos += 1

  return found

# For ordered/sorted list/array
def ordered_seq_search(arr, element):
  pos = 0
  found = False  # This variable will become True when we get the element.
  stopped = False  # To make sure we iterate till we get the element or just greater than the element and hance avoivding full array search
  while pos < len(arr) and not found and not stopped:

    if arr[pos] == element:
      found = True

    else:
      if arr[pos] > element:
        stopped = True
      else:
        pos += 1

  return found


arr1 = [1, 2, 6, 4, 5, 9, 3]
print(seq_search(arr1, 5))
arr2 = [1, 2, 3, 4, 5, 6, 9]
print(ordered_seq_search(arr2, 8))

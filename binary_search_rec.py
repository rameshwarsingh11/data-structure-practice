# Binary Search recursive
def binary_search_rec(arr, ele):
  # Checking edge case first
  if len(arr) == 0:
    return False

  # recursive call
  else:
    mid = int(len(arr)/2)

    if arr[mid] == ele:
      return True

    else:
      if ele < arr[mid]:
        return binary_search_rec(arr[:mid], ele)

      else:
        return binary_search_rec(arr[mid+1:], ele)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search_rec(arr, 13))

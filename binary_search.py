# Binary Search
# Assuming the list/array is sorted
# Method binary search, passing the given array and the element to be searched
def binary_search(arr, ele):
  first = 0  # first index to zero
  last = len(arr) - 1  # setting last index to last element pointer

  found = False

  while first <= last and not found:

    mid = int((first+last)/2)

    if arr[mid] == ele:
      found = True
    else:
        if ele < arr[mid]:
          last = mid-1

        else:
          first = mid + 1

  return found

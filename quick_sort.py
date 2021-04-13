# Quick Sort in Python

def quick_sort(arr):

    quick_sort_helper(arr, 0, len(arr)-1)

def quick_sort_helper(arr, first, last):
  if first < last:
    splitpoint = partition(arr, first, last)
    # Recursive calls
    # On first half
    quick_sort_helper(arr, first, splitpoint-1)
    # On last half
    quick_sort_helper(arr, splitpoint+1, last)


def partition(arr, first, last):
  pivotvalue = arr[first]

  leftmark = first + 1
  rightmark = last

  done = False

  while not done:
    while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
      # Moving the left mark to the right until we locate the value which is greater than the pivot value
      leftmark += 1

    while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
      # Moving the right mark to the left until we find a value which is less than the pivot.
      rightmark -= 1

    if rightmark < leftmark:  # Means rightmark and leftmark have crossed each other
      done = True

    else:
      # Exchange the values on the correct side of pivot
      temp = arr[leftmark]
      arr[leftmark] = arr[rightmark]
      arr[rightmark] = temp

  temp = arr[first]
  arr[first] = arr[rightmark]
  arr[rightmark] = temp

  return rightmark


arr = [34, 6, 5, 7, 8, 90, 1]
print('Unsorted Array :::', arr)
quick_sort(arr)
print('Sorted Array :::', arr)
